from xor.xor import (
    clear_screen,
    xor,
    gen_key_stream
)

def main() -> None:
     message = input("your message to encrypt/decrypt: ")
     clear_screen()
     key = gen_key_stream(n=len(message))
     key_int = int.from_bytes(key, byteorder="big")

     cipher = xor(key_stream=key, message=message)
     cipher_int = int.from_bytes(cipher, byteorder="big")

     print(f"never print your key lol:\n{key}")
     print(key_int)
     print()
     print(f"cipher:\n{cipher}")
     print(cipher_int)

if __name__ == "__main__":
    main()