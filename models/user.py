from datetime import datetime
from utils.crypto import generate_uuid, generate_key_pair

class UserRole:
    ADMIN = "admin"
    MANUFACTURER = "manufacturer"
    DISTRIBUTOR = "distributor"
    DENTAL_CLINIC = "dental_clinic"
    DENTIST = "dentist"
    MAINTENANCE_STAFF = "maintenance_staff"
    REGULATOR = "regulator"

class User:
    def __init__(self, username, email, role, organization=None):
        self.id = generate_uuid()
        self.username = username
        self.email = email
        self.role = role
        self.organization = organization
        self.public_key, self.private_key = generate_key_pair()
        self.created_at = datetime.now()
        self.last_login = None
    
    def sign_transaction(self, transaction):
        """Sign a transaction with the user's private key"""
        # In a real application, this would use the private key to sign
        transaction.sign(f"Signed by {self.username}")
        return transaction
    
    def to_dict(self):
        """Convert the user to a dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'organization': self.organization,
            'public_key': self.public_key,
            'created_at': self.created_at,
            'last_login': self.last_login
        }