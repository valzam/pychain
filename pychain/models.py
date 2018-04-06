from Crypto.Hash import SHA3_256
from Crypto.Signature import pkcs1_15

class Block:
    def __init__(self, prev_hash, transactions, difficulty):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.difficulty = difficulty
        self.block_hash = None
        self.nonce = 0
    
    def mine(self):
        """Convenience function for creating a block.
        It automatically creates a hash of the transactions and runs until it has found a
        nonce that creates a hash appropriate for the difficulty.
        Returns True once the hash has been found and saves all details of the block
        """

        return True
    
    def create_hash(self) -> str:
        """Creates a hash of the current block using SHA3_256
        
        Returns:
            str -- block hash
        """

        return ""
    
    def check_nonce(self) -> bool:
        """Checks if the current nonce creates a hash that satisfies the difficulty condition
        
        Returns:
            bool -- True if hash has self.difficulty leading 0s
        """

        return False


        
class Transaction:
    def __init__(self, value, receiver, sender):
        self.value = value
        self.receiver = receiver
        self.sender = sender
        self.signature = None
        
    def create_hash(self) -> SHA3_256:
        """Create a hash of the transaction value, receiver and sender
        
        Returns:
            SHA3_256 -- SHA3_256 object
        """
        h_obj = SHA3_256.new()
        h_obj.update(str.encode(f"{self.value}{self.receiver}{self.sender}"))

        return h_obj
    
    def sign(self, private_key):
        """Signs the transaction with the sender's private key
        
        Arguments:
            private_key {RSA Key} -- RSA private key
        """
        transaction_hash_obj = self.create_hash()
        self.signature = pkcs1_15.new(private_key).sign(transaction_hash_obj)

    def __repr__(self) -> str:
        if not self.signature:
            raise UnsignedTransactionError()
        return f"{self.value}-{self.receiver}-{self.sender}-{self.signature}"


class UnsignedTransactionError(Exception):
    pass

    
