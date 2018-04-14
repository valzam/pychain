import unittest
from pychain import models
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_256
import binascii


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.key = RSA.import_key(open('tests/test_rsa').read())
        self.key_pub = RSA.import_key(open('tests/test_rsa.pub').read())
        self.key_pub = binascii.hexlify(self.key_pub.exportKey(format="DER"))
        self.t = models.Transaction(value=10, receiver=self.key_pub, sender=self.key_pub)

    def test_unsigned_exception(self):
        with self.assertRaises(models.UnsignedTransactionError):
            str(self.t)

    def test_creating_hash(self):
        h_obj = SHA3_256.new()
        h_obj.update(str.encode(f"{self.t.value}{self.t.receiver}{self.t.sender}"))
        h_hex = h_obj.hexdigest()

        self.assertEqual(h_hex, self.t.create_hash().hexdigest())

    def test_signature(self):
        self.t.sign(self.key)
        h_obj = SHA3_256.new()
        h_obj.update(str.encode(f"{self.t.value}{self.t.receiver}{self.t.sender}"))
        signature = models.pkcs1_15.new(self.key).sign(h_obj)
        signature = binascii.hexlify(signature)
        self.assertEqual(signature, self.t.signature)

    def test_signed_representation(self):
        self.t.sign(self.key)
        signature = self.t.signature
        str_rep = str(self.t)
        expected = f"10-{str(self.key_pub)}-{str(self.key_pub)}-{signature}"
        self.assertEqual(str_rep, expected)


class TestBlock(unittest.TestCase):
    def setUp(self):
        t = models.Transaction(value=10, receiver="r", sender="s")
        self.keyr = RSA.import_key(open('tests/test_rsa').read())
        t.sign(self.keyr)
        self.transactions = [str(t)]
        self.prev_hash = SHA3_256.new().update(str.encode("fake previous block")).hexdigest()
        self.difficulty = 1
        self.block = models.Block(prev_hash=self.prev_hash, transactions=self.transactions, difficulty=self.difficulty)

    def test_create_hash(self):
        nonce = 0
        str_concat = "".join(self.transactions)
        hash_preimage = str.encode(f"{self.prev_hash}{nonce}{self.difficulty}{str_concat}")

        h_obj = SHA3_256.new()
        h_obj.update(hash_preimage)
        h_hex = h_obj.hexdigest()
        self.assertEqual(h_hex, self.block.create_hash().hexdigest())

    def test_check_nonce(self):
        # Hash of testblock is c5e3b1b8b292aaa9d397d18a7c9d5fb05c56c631c9f5fd6bd97f9992fbd58b2b with nonce 0
        self.assertFalse(self.block.check_nonce())

        # Nonce 8 satisfies the conditions 049655763dbfda29978f099d3856249670b41e2beb27f00fe249a02498aa65a1
        self.block.mine()
        self.assertTrue(self.block.check_nonce())

    def test_mine(self):
        self.block.mine()

        self.assertTrue(self.block.nonce_found)



