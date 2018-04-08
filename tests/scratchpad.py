from pychain import models
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_256
t = models.Transaction(value=10, receiver="r", sender="s")
keyr =  RSA.import_key(open('tests/test_rsa').read())
t.sign(keyr)
transactions = [str(t)]
prev_hash = SHA3_256.new().update(str.encode("fake previous block")).hexdigest()
difficulty = 1
block = models.Block(prev_hash=prev_hash, transactions=transactions, difficulty=difficulty)