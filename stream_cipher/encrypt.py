from stream_cipher.stream_cipher import (
    clear_screen,
    KeyStream,
    xor
)

def main() -> None:
    message = input("your message to encrypt: ")
    seed = int(input("seed: "))
    clear_screen()

    key  = KeyStream(seed)
    cipher = xor(key_stream=key, message=message)
    cipher_int = int.from_bytes(cipher, byteorder="big")

    print(f"cipher: {cipher}\n")
    print(f"cipher_int: {cipher_int}\n")

    return None

if __name__ == "__main__":
    main()