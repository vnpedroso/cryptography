from xor.xor import xor

def main() -> None:

    cipher = int(input("your cipher: "))
    key = int(input("your key: "))
    message = xor(key_stream=key, message=cipher)
    print(message)

if __name__ == "__main__":
    main()