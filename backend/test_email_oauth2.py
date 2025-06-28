import os
import sys
from flask import Flask
from config import get_config

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the OAuth2 email service
from utils.email_service_oauth2 import test_gmail_oauth2, gmail_service

def main():
    """Test Gmail OAuth2 email configuration."""
    
    # Create Flask app for testing
    app = Flask(__name__)
    app.config.from_object(get_config())
    
    with app.app_context():
        print("=== Gmail OAuth2 Email Test ===")
        print(f"Credentials file: {app.config.get('GOOGLE_CREDENTIALS_FILE')}")
        print(f"Token file: {app.config.get('GOOGLE_TOKEN_FILE')}")
        print(f"Gmail user: {app.config.get('GMAIL_USER_EMAIL')}")
        print()
        
        # Check if credentials file exists
        creds_file = app.config.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        if not os.path.exists(creds_file):
            print(f"❌ Credentials file not found: {creds_file}")
            print()
            print("Setup Instructions:")
            print("1. Go to https://console.cloud.google.com/")
            print("2. Create a new project or select existing project")
            print("3. Enable Gmail API")
            print("4. Create OAuth2 credentials (Desktop application)")
            print("5. Download the credentials JSON file")
            print("6. Rename it to 'credentials.json' and place in backend folder")
            print("7. Update .env file with your Gmail address")
            return
        
        print("Credentials file found ✅")
        print()
        
        # Test authentication
        print("Testing OAuth2 authentication...")
        try:
            if gmail_service.authenticate():
                print("Authentication successful ✅")
                print()
                
                # Test sending email
                print("Testing email sending...")
                test_gmail_oauth2()
            else:
                print("Authentication failed ❌")
        except Exception as e:
            print(f"Error during authentication: {e}")
            print()
            print("Troubleshooting:")
            print("- Make sure you have the correct credentials.json file")
            print("- Check that your Gmail account has 2FA enabled")
            print("- Verify that Gmail API is enabled in Google Cloud Console")

if __name__ == "__main__":
    main()