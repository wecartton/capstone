from flask import current_app
from flask_mail import Mail

# Import OAuth2 service
from utils.email_service_oauth2 import send_password_reset_email as send_oauth2_email
from utils.email_service_oauth2 import gmail_service

# Keep Flask-Mail for backward compatibility
mail = Mail()

def send_password_reset_email(to_email, reset_url):
    """Send a password reset email.
    
    Primary method: Gmail OAuth2
    Fallback method: Traditional SMTP (if configured)
    """
    
    print(f"Attempting to send password reset email to: {to_email}")
    
    # Check if OAuth2 is configured
    google_creds = current_app.config.get('GOOGLE_CREDENTIALS_FILE')
    if google_creds:
        print("Using Gmail OAuth2...")
        try:
            return send_oauth2_email(to_email, reset_url)
        except Exception as e:
            print(f"OAuth2 sending failed: {e}")
            print("Falling back to traditional SMTP...")
    
    # Fallback to traditional SMTP if OAuth2 not available or fails
    print("Using traditional SMTP...")
    return send_password_reset_email_fallback(to_email, reset_url)

def send_password_reset_email_fallback(to_email, reset_url):
    """Fallback function using Flask-Mail."""
    from flask_mail import Message
    
    subject = "Reset Your ELLC Password"
    body = f"""
    Hello,

    You have requested to reset your password for your ELLC account.
    Please click the link below to reset your password:

    {reset_url}

    This link will expire in 24 hours.

    If you did not request a password reset, please ignore this email.

    Best regards,
    The ELLC Team
    """
    
    try:
        msg = Message(
            subject,
            recipients=[to_email],
            body=body,
            sender=current_app.config.get('MAIL_DEFAULT_SENDER', 'noreply@ellcsystem.com')
        )
        mail.send(msg)
        print("Email sent successfully using Flask-Mail!")
        return True
    except Exception as e:
        print(f"Error sending email via Flask-Mail: {str(e)}")
        return False