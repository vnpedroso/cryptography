from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 

def main() -> None:
    key = get_random_bytes(8) # 64 bits key
    data = b"0123456701234567" # repetitive message showing the ECB weakness
    
    des_system = des(key)
    cipher = encrypt(data=data, des_system=des_system)
    print(f"\ncipher: {cipher}")

    des_system = des(key) #encryption systems as non-reusable stateful objects
    message = decrypt(cipher=cipher, des_system=des_system)
    print(f"\nmessage: {message}")

    return None

def des(key: bytes) -> object:
    return DES.new(key, DES.MODE_ECB)

def encrypt(data: bytes, des_system: object) -> bytes:
    return des_system.encrypt(pad(data, 16))

def decrypt(cipher: bytes, des_system: object) -> bytes:
    return unpad(des_system.decrypt(cipher), 16) #try it without unpading!

if __name__ == '__main__':
    main()