from caesar_cipher.caesar_cipher import (
    encrypt,
    generate_key
)

def main() -> None:

    cipher = str(input("\nyour cipher: ")).upper()
    assert cipher != "", "no cipher inputted - please write your cipher"

    for i in range(26):
        dkey = generate_key(i)
        message = encrypt(dkey,cipher)
        print(message)
    return None

if __name__ == "__main__":
    main()