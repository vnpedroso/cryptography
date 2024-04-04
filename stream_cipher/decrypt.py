from stream_cipher.stream_cipher import (
    clear_screen,
    KeyStream,
    xor
)

def main() -> None:
    message = int(input("your cipher to decrypt: "))
    seed = int(input("seed: "))
    clear_screen()

    key = KeyStream(seed)
    decrypted_cipher = xor(key_stream=key, message=message)
    print(f"decrypted cipher: {decrypted_cipher.decode()}\n")

    return None

if __name__ == "__main__":
    main()

