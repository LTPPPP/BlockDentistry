import hashlib

class ProofOfWork:
    @staticmethod
    def find_proof(previous_proof, difficulty='0000'):
        """
        Find a proof that satisfies the difficulty requirement
        """
        new_proof = 1
        check_proof = False
        
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:len(difficulty)] == difficulty:
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    @staticmethod
    def is_valid_proof(previous_proof, proof, difficulty='0000'):
        """
        Check if the proof satisfies the difficulty requirement
        """
        hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
        return hash_operation[:len(difficulty)] == difficulty