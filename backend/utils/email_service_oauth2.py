import os
import json
import pickle
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from flask import current_app
from flask_mail import Mail

# Gmail API scope untuk mengirim email
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Keep Flask-Mail for backward compatibility
mail = Mail()

class GmailOAuth2Service:
    def __init__(self):
        self.creds = None
        self.service = None
        
    def authenticate(self):
        """Authenticate dengan Gmail using OAuth2."""
        credentials_file = current_app.config.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        token_file = current_app.config.get('GOOGLE_TOKEN_FILE', 'token.pickle')
        
        print(f"Looking for credentials file: {credentials_file}")
        print(f"Looking for token file: {token_file}")
        
        # Load existing token jika ada
        if os.path.exists(token_file):
            print("Loading existing token...")
            with open(token_file, 'rb') as token:
                self.creds = pickle.load(token)
        
        # Jika tidak ada valid credentials, lakukan OAuth flow
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                print("Refreshing expired token...")
                try:
                    self.creds.refresh(Request())
                except Exception as e:
                    print(f"Error refreshing token: {e}")
                    self.creds = None
            
            # Jika masih tidak ada valid credentials, lakukan OAuth flow
            if not self.creds:
                print("Starting OAuth flow...")
                if not os.path.exists(credentials_file):
                    raise FileNotFoundError(f"Credentials file not found: {credentials_file}")
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES)
                # Use local server untuk OAuth callback
                self.creds = flow.run_local_server(port=8080)
            
            # Save credentials untuk penggunaan berikutnya
            print("Saving credentials...")
            with open(token_file, 'wb') as token:
                pickle.dump(self.creds, token)
        
        # Build Gmail service
        self.service = build('gmail', 'v1', credentials=self.creds)
        print("Gmail OAuth2 authentication successful!")
        return True
    
    def create_message(self, to_email, subject, body_text, body_html=None):
        """Create a message for an email."""
        
        if body_html:
            # Create multipart message for HTML + text
            message = MIMEMultipart('alternative')
            text_part = MIMEText(body_text, 'plain')
            html_part = MIMEText(body_html, 'html')
            message.attach(text_part)
            message.attach(html_part)
        else:
            # Create simple text message
            message = MIMEText(body_text)
        
        message['to'] = to_email
        message['subject'] = subject
        message['from'] = current_app.config.get('GMAIL_USER_EMAIL')
        
        # Encode message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw_message}
    
    def send_message(self, to_email, subject, body_text, body_html=None):
        """Send an email message via Gmail API."""
        try:
            # Ensure we're authenticated
            if not self.service:
                if not self.authenticate():
                    return False
            
            # Create message
            message = self.create_message(to_email, subject, body_text, body_html)
            
            # Send message
            print(f"Sending email to {to_email} via Gmail API...")
            result = self.service.users().messages().send(
                userId='me', body=message).execute()
            
            print(f"Email sent successfully! Message ID: {result['id']}")
            return True
            
        except HttpError as error:
            print(f"Gmail API error: {error}")
            return False
        except Exception as error:
            print(f"An error occurred: {error}")
            return False

# Global Gmail service instance
gmail_service = GmailOAuth2Service()

def send_password_reset_email(to_email, reset_url):
    """Send a password reset email using Gmail OAuth2."""
    
    print(f"Attempting to send email via Gmail OAuth2 to: {to_email}")
    print(f"Reset URL: {reset_url}")
    
    # Email content
    subject = "Reset Your ELLC Password"
    
    # Plain text content
    body_text = f"""
Hello,

You have requested to reset your password for your ELLC account.
Please click the link below to reset your password:

{reset_url}

This link will expire in 24 hours.

If you did not request a password reset, please ignore this email.

Best regards,
The ELLC Team
    """.strip()
    
    # HTML content
    body_html = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #1e3a5f;">Reset Your ELLC Password</h2>
        <p>Hello,</p>
        <p>You have requested to reset your password for your ELLC account.</p>
        <p>Please click the button below to reset your password:</p>
        <div style="text-align: center; margin: 30px 0;">
            <a href="{reset_url}" 
               style="background-color: #007bff; color: white; padding: 12px 30px; 
                      text-decoration: none; border-radius: 5px; display: inline-block;">
                Reset Password
            </a>
        </div>
        <p>Or copy and paste this link into your browser:</p>
        <p style="word-break: break-all; color: #666;">{reset_url}</p>
        <p style="color: #888; font-size: 14px; margin-top: 30px;">
            This link will expire in 24 hours. If you did not request a password reset, 
            please ignore this email.
        </p>
        <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
        <p style="color: #888; font-size: 14px;">
            Best regards,<br>
            The ELLC Team
        </p>
    </div>
</body>
</html>
    """.strip()
    
    # Send email
    return gmail_service.send_message(to_email, subject, body_text, body_html)

# Test function
def test_gmail_oauth2():
    """Test Gmail OAuth2 setup."""
    
    test_email = input("Enter test email: ").strip()
    if not test_email:
        test_email = "test@example.com"
    
    test_url = "http://localhost:3000/reset-password/test-token-123"
    
    success = send_password_reset_email(test_email, test_url)
    
    if success:
        print("✅ Test email sent successfully!")
    else:
        print("❌ Test email failed!")
    
    return success