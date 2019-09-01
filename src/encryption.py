from secrets import token_bytes
from typing import Tuple


def random_key(lenght: int) -> int:
    """Return a random bit string of length."""
    tb: bytes = token_bytes(lenght)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    """Encrypt a string into a dummy and a secret bit string."""
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    secret: int = original_key ^ dummy
    return (dummy, secret)


def decrypt(key1: int, key2: int) -> str:
    """Decrypt using the two keys and return the resulting string."""
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    dummy, encrypted = encrypt("Hi bro!")
    print(encrypted, dummy)
    result = decrypt(dummy, encrypted)
    print(result)
