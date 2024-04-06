from vinegere_cipher.oop_vinegere_cipher import(
    VinegereEngine,
    decrypt,
    clear_screen
)

def main() -> None:
    key = input("enter your key: ")
    ve = VinegereEngine(key)

    cipher = input("enter your cipher: ")
    clear_screen()
    message = decrypt(key_engine=ve, cipher=cipher)

    print(f"message: {message}")

    return None

if __name__ == "__main__":
    main()