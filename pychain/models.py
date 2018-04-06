from Crypto.Hash import SHA3_256

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
        
    def create_hash(self) -> str:
        """Create a hash of the transaction value and receiver
        
        Returns:
            str -- hexdigest of SHA3_256 hash
        """

        return ""
    
    def sign(self, private_key):
        """Signs the transaction with the sender's private key
        
        Arguments:
            private_key {string} -- 32 bit private key as hexdigest
        """

        self.signature = "signed"

    def __repr__(self) -> str:
        if not self.signature:
            raise UnsignedTransactionError()
        return f"{self.value} - {self.receiver} - {self.sender} - {self.signature}"


class UnsignedTransactionError(Exception):
    pass

    
