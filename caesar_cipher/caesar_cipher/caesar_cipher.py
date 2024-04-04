import os
import platform

def generate_key(n: int) -> dict:
    #mapping all letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # let's keep it upper case
    key = {} # let's benefit from the 1:1 relationship of key-valued pairs...
    counter = 0 # this counter will be important later on!

    for char in letters:
        key[char] = letters[(counter + n) % len(letters)]
        # by adding module of len(letters) we assure that the counter always stays between the letters!
        # if the number is smaller than 26, it returns itself
        # if the number is bigger, we get the closet 26 multiple plus the difference
        # and yes, that difference is always a number between 0 and 26 
        counter += 1
    
    return key

    
def generate_dkey(key: dict) -> dict:
    dkey = {}
    for char in key: # a simple reversion of the key dictionary
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

