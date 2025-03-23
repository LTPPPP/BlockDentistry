import time
import json
from utils.crypto import calculate_hash

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, proof=None):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.proof = proof

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }
    
    def calculate_hash(self):
        """Calculate hash of the block"""
        block_string = json.dumps(self.to_dict(), sort_keys=True)
        return calculate_hash(block_string)