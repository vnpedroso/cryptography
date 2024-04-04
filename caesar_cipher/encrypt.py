from caesar_cipher.caesar_cipher import (
    encrypt, 
    generate_key, 
    clear_screen
)

from secrets import randbelow

def main() -> None:
    message = str(input("\nyour message: ")).upper()
    clear_screen()
    assert message != "", "no message inputted - please write your message"

    key_number = (randbelow(1001))
    key = generate_key(key_number)
    cipher = encrypt(key,message)

    print(key_number)
    print(cipher)
    
    return None

if __name__ == "__main__":
    main()

