import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from files.clear import clear

def key():
    with open(".data/temp_file.txt", "r") as tf:
        raw_passwd = tf.read()

    password = raw_passwd.encode()

    mysalt = b'\xbb\x9c\xdfu\xee\x99\xe3e\xce\x9e\xff*\xb3):r'

    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256,
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()
    )

    encoded_key = base64.urlsafe_b64encode(kdf.derive(password))

    key = encoded_key.decode()
    return key

key_name = key()
