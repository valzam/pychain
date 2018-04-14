from pychain import models
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_256

keyr = RSA.import_key(open('tests/test_rsa').read())
key_pub = RSA.import_key(open('tests/test_rsa.pub').read())
key_pub = binascii.hexlify(key_pub.exportKey(format="DER"))
t = models.Transaction(value=10, receiver=key_pub, sender=key_pub)
t.sign(keyr)
print(t)