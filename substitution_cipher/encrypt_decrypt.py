from substitution_cipher.substitution_cipher import (
    encrypt, 
    generate_key, 
    generate_dkey
)

def main() -> None:
    message = str(input("\nyour message: ")).upper()
    assert message != "", "no message inputted - please write your messsage"

    key = generate_key()
    print("\nstarting encryption...")
    cipher = encrypt(key, message)
    print(cipher)

    dkey = generate_dkey(key)
    decrypted_message = encrypt(dkey, cipher)
    print("\nstarting decryption..")
    print(decrypted_message)

    print("\nnever print your key lol")
    print(key)

if __name__ == "__main__":
    main()
