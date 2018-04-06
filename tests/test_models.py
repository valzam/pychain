import unittest
from pychain import models

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.t = models.Transaction(10, "r", "s")
    def test_unsigned_exception(self):
        with self.assertRaises(models.UnsignedTransactionError):
            str(self.t)

    def test_signed_representation(self):
        self.t.sign("private_key")
        str_rep = str(self.t)
        expected = "10 - r - s - signed"
        self.assertEqual(str_rep, expected)