import unittest
from pychain import models, node
from Crypto.PublicKey import RSA


class TestNode(unittest.TestCase):
    def setUp(self):
        self.t = models.Transaction(value=10, receiver="r", sender="s")
        self.keyr = RSA.import_key(open('tests/test_rsa').read())
        self.t.sign(self.keyr)
        self.node = node.Node()

    def test_accept_transaction(self):
        self.node.accept_transaction(str(self.t))

        self.assertEqual(len(self.node.mem_pool), 1)

    def test_mine_block(self):
        for i in range(5):
            self.node.accept_transaction(str(self.t))    

        self.node.mine_block()
        self.assertEqual(len(self.node.blockchain), 1)