from datetime import datetime
from utils.crypto import generate_uuid

class TransactionType:
    NEW_EQUIPMENT = "new_equipment"
    TRANSFER = "transfer"
    MAINTENANCE = "maintenance"
    STERILIZATION = "sterilization"
    CERTIFICATION = "certification"
    STATUS_UPDATE = "status_update"
    DISPOSAL = "disposal"

class Transaction:
    def __init__(self, transaction_type, equipment_id, sender, receiver=None, 
                 details=None, timestamp=None):
        self.id = generate_uuid()
        self.transaction_type = transaction_type
        self.equipment_id = equipment_id
        self.sender = sender
        self.receiver = receiver
        self.details = details or {}
        self.timestamp = timestamp or datetime.now()
        self.signature = None
    
    def sign(self, signature):
        """Sign the transaction"""
        self.signature = signature
    
    def to_dict(self):
        """Convert the transaction to a dictionary"""
        return {
            'id': self.id,
            'transaction_type': self.transaction_type,
            'equipment_id': self.equipment_id,
            'sender': self.sender,
            'receiver': self.receiver,
            'details': self.details,
            'timestamp': self.timestamp,
            'signature': self.signature
        }