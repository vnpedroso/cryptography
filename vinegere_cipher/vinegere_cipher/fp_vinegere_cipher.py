import os 
import platform
from collections.abc import Generator
from string import ascii_lowercase

def _key_rotor(key: str) -> Generator[str]:
    for i in key:
        assert i in ascii_lowercase, f"{i} ::: item is not part of this alphabet"
    while True:
        for i in key:
            yield i


def encrypt(gen: Generator, data: str) -> str:
    alphabet = ascii_lowercase
    cipher = "" 
    for i in data:
        if i in alphabet:
            index = (alphabet.find(i) + alphabet.find(next(gen))) % len(alphabet)
            cipher += alphabet[index]
        else:
            cipher += i
    return cipher

def decrypt(gen: Generator, cipher: str) -> str:
    alphabet = ascii_lowercase
    data = "" 
    for i in cipher:
        if i in alphabet:
            index = (alphabet.find(i) - alphabet.find(next(gen))) % len(alphabet)
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

