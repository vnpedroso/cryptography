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
    intercepted_cipher = interception_attack(cipher=cipher)
    
    decrypyed_cipher = xor(key_stream=key, message=intercepted_cipher)
    print(f"decrypted cipher: {decrypyed_cipher.decode('utf-8')}\n")

    return None

def interception_attack(cipher: bytes | int) -> bytes:
    """we are assuming the attacker has context on that communication and can guess the mesage"""
    if isinstance(cipher, int):
        cipher = cipher.to_bytes((cipher.bit_length() + 7) // 8, "big")

    modifier = [0]*len(cipher)
    modifier[9] = ord("4") ^ ord("9")
    modifier[10] = ord("5") ^ ord("9")

    return bytes([modifier[i] ^ cipher[i] for i in range(len(cipher))])

if __name__ == "__main__":
    main()

