import time
from blockchain.block import Block
from blockchain.proof_mechanisms import ProofOfWork
from utils.crypto import calculate_hash

class Blockchain:
    def __init__(self, difficulty='0000'):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = difficulty
        # Genesis block
        self.create_block(proof=1, previous_hash='0')
        
    def create_block(self, proof, previous_hash):
        """Create a new block and add it to the chain"""
        block = Block(
            index=len(self.chain) + 1,
            transactions=self.pending_transactions,
            timestamp=time.time(),
            previous_hash=previous_hash,
            proof=proof
        )
        
        self.pending_transactions = []
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        """Find a proof that satisfies our criteria"""
        return ProofOfWork.find_proof(previous_proof, self.difficulty)
    
    def hash(self, block):
        """Hash a block"""
        return block.calculate_hash()
    
    def is_chain_valid(self):
        """Check if the blockchain is valid"""
        previous_block = self.chain[0]
        block_index = 1
        
        while block_index < len(self.chain):
            block = self.chain[block_index]
            # Check if the previous hash is correct
            if block.previous_hash != self.hash(previous_block):
                return False
            
            # Check if the proof of work is correct
            if not ProofOfWork.is_valid_proof(previous_block.proof, block.proof, self.difficulty):
                return False
            
            previous_block = block
            block_index += 1
        
        return True
    
    def add_transaction(self, transaction):
        """Add a transaction to the pending transactions list"""
        self.pending_transactions.append(transaction.to_dict())
        return self.get_previous_block().index + 1
    
    def get_chain_data(self):
        """Return the chain data in a serializable format"""
        return {
            'chain': [block.to_dict() for block in self.chain],
            'length': len(self.chain)
        }