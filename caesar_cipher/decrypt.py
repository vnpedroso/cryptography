from caesar_cipher.caesar_cipher import (
    encrypt, 
    generate_key, 
    generate_dkey
    )

def main() -> None:
    cipher = str(input("\nyour cipher: ")).upper()
    assert cipher != "", "no cipher inputted - please write your cipher"

    key_number = int(input("encryption key number: "))
    assert isinstance(key_number, int), "please write a valid integer number!"

    key = generate_key(key_number)
    print("\nstarting decryption: \n")

    dkey = generate_dkey(key)
    decrypted_message = encrypt(dkey,cipher)
    print(decrypted_message)

if __name__ == "__main__":
    main()
