import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


class InvalidPasswordError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Encryption:

    def __init__(self, password):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            iterations=480000,
            salt=b'great'
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password))
        
        self.fernet = Fernet(key)

    def encrypt(self, data):
        return self.fernet.encrypt(data)

    def decrypt(self, data):
        return self.fernet.decrypt(data)

