from secrets import randbelow

from stream_cipher.stream_cipher import (
    clear_screen,
    KeyStream,
    xor
)

def main() -> None:
    cipher = int(input("your cipher to decrypt: "))
    seed = int(input("seed: "))
    clear_screen()

    key = KeyStream(seed)
    transmitted_cipher = faulty_transmisson(cipher=cipher, inverse_prob=10)

    decrypted_cipher = xor(key_stream=key, message=transmitted_cipher)
    print(f"decrypted cipher: {decrypted_cipher.decode()}\n")

    return None

def faulty_transmisson(cipher: bytes | int, inverse_prob: int) -> bytes:
    if isinstance(cipher, int):
        cipher = cipher.to_bytes((cipher.bit_length() + 7) // 8, "big")
        print(cipher)

    transmitted_cipher = []
    for char in cipher:
        if randbelow(inverse_prob) == 0:
            char = char ^ (2 ** randbelow(8))
        transmitted_cipher.append(char)
    
    return bytes(transmitted_cipher)

if __name__ == "__main__":
    main()