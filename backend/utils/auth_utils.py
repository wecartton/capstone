import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from flask import current_app

def get_encryption_key():
    """Get or generate a Fernet key for encryption."""
    # In production, use an environment variable for the secret key
    key = current_app.config.get('SECRET_KEY', 'default-secret-key')
    salt = b'ellc-system-salt'  # In production, use a secure random salt
    
    # Generate a key from the secret key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    # Generate the key
    key_bytes = kdf.derive(key.encode())
    return base64.urlsafe_b64encode(key_bytes)

def encrypt_data(data):
    """Encrypt sensitive data."""
    if not data:
        return None
        
    fernet = Fernet(get_encryption_key())
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    """Decrypt encrypted data."""
    if not encrypted_data:
        return None
        
    fernet = Fernet(get_encryption_key())
    return fernet.decrypt(encrypted_data.encode()).decode()

