import os 
import platform
from secrets import randbelow

def generate_key() -> dict: 
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    listed_letters = list(letters)
    key = {}
    for char in letters:
        key[char] = listed_letters.pop(randbelow(len(listed_letters)))
    return key

def generate_dkey(key: dict) -> bytes:
    dkey = {}
    for char in key:
        dkey[key[char]] = char
    return dkey

def encrypt(key, message) -> str:
    cipher = ""
    for char in message:
        if char in key.keys():
            cipher += key[char]
        else:
            cipher += char

    return cipher

def clear_screen() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return None
