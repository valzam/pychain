import unittest
from pychain import models
from Crypto.PublicKey import RSA

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.t = models.Transaction(10, "r", "s")
        self.key =  RSA.import_key(open('tests/test_rsa').read())

    def test_unsigned_exception(self):
        with self.assertRaises(models.UnsignedTransactionError):
            str(self.t)

    def test_creating_hash(self):
        h_obj = models.SHA3_256.new()
        h_obj.update(str.encode(f"{self.t.value}{self.t.receiver}{self.t.sender}"))
        h_hex = h_obj.hexdigest()

        self.assertEqual(h_hex, self.t.create_hash().hexdigest())

    def test_signature(self):
        self.t.sign(self.key)
        h_obj = models.SHA3_256.new()
        h_obj.update(str.encode(f"{self.t.value}{self.t.receiver}{self.t.sender}"))
        signature = models.pkcs1_15.new(self.key).sign(h_obj)

        self.assertEqual(signature, self.t.signature)


    def test_signed_representation(self):
        self.t.sign(self.key)
        signature = self.t.signature
        str_rep = str(self.t)
        expected = f"10-r-s-{signature}"

        self.assertEqual(str_rep, expected)


class TestBlock(unittest.TestCase):
    def setUp(self):
        t = models.Transaction(10, "r", "s")
        t.sign(self.key)
        transactions = [str(t)]