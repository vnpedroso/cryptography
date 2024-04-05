import os 
import platform
from string import ascii_lowercase

class VinegereEngine() :
    def __init__(self, key: str) -> None:
        for n,i in enumerate(key):
            assert i.lower() in ascii_lowercase, f"key[{n}] = {i} ::: item is not part of this alphabet"
        self.key = key.lower()
        self._next_key = self._key_rotor()

    def _key_rotor(self):
        while True:
            for i in self.key:
                yield i

    @property
    def next_key(self):
        return next(self._next_key)


def encrypt(key_engine: object, data: str) -> str:
    alphabet = ascii_lowercase
    cipher = "" 
    for i in data:
        if i in alphabet:
            index = (alphabet.find(i) + alphabet.find(key_engine.next_key)) % len(alphabet)
            cipher += alphabet[index]
        else:
            cipher += i
    return cipher

def decrypt(key_engine: object, cipher: str) -> str:
    alphabet = ascii_lowercase
    data = "" 
    for i in cipher:
        if i in alphabet:
            index = (alphabet.find(i) - alphabet.find(key_engine.next_key)) % len(alphabet)
            data += alphabet[index]
        else:
            data += i
    return data

def clear_screen() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return None