import hashlib
import hmac
import secrets
from dataclasses import dataclass


@dataclass
class Passwords:
    salt: bytes
    digest: bytes

    @classmethod
    def create(cls, password):
        salt = secrets.token_bytes(16)
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
        return cls(salt=salt, digest=digest)

    def verify(self, password):
        candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), self.salt, 200_000)
        return hmac.compare_digest(candidate, self.digest)
