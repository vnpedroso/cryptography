from vinegere_cipher.oop_vinegere_cipher import(
    VinegereEngine,
    encrypt,
    clear_screen
)

def main() -> None:
    key = input("enter your key: ")
    ve = VinegereEngine(key)

    message = input("enter your message: ")
    clear_screen()
    cipher = encrypt(key_engine=ve, data=message)

    print(f"cipher: {cipher}")

    return None

if __name__ == "__main__":
    main()