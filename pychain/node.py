from pychain import models
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Node:
    def __init__(self):
        self.mem_pool = []
        self.blockchain = []
        self.max_mem_pool = 3
        self.difficulty = 1
    
    def accept_transaction(self, transaction: str):
        self.mem_pool.append(transaction)
        logger.info("Accepted a new transaction")
        if len(self.mem_pool) >= self.max_mem_pool:
            self.mine_block()
    
    def mine_block(self) -> bool:
        """This method starts the mining process for a new block.
        It packages all transactions in the mempool into a block, mines it and appends
        the new block to the blockchain
        
        Returns:
            bool -- Indicator that the mining was successful
        """
        logger.info("Mining a new block")
        if len(self.blockchain) == 0:
            prev_hash = "genesis"
        else:
            prev_hash = self.blockchain[-1].block_hash
        new_block = models.Block(prev_hash=prev_hash, transactions=self.mem_pool,
                                 difficulty=self.difficulty)

        new_block.mine()
        self.blockchain.append(new_block)
        self.mem_pool = []

        return True