from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 

def main() -> None:
    key = get_random_bytes(8) # 64 bits key
    iv = get_random_bytes(8) # 64 bits initialization vector
    data = b"0123456701234567" # same repetitive pattern as the EBC mode
    
    des_system = des_cbc(key=key, iv=iv)
    cipher = encrypt(data=data, des_system=des_system)
    print(f"\ncipher: {cipher}")

    #encryption systems as non-reusable stateful objects
    des_system = des_cbc(key=key, iv=iv)
    message = decrypt(cipher=cipher, des_system=des_system)
    print(f"\nmessage: {message}")

    return None

def des_cbc(key: bytes, iv: bytes) -> object:
    return DES.new(key, DES.MODE_CBC, iv)

def encrypt(data: bytes, des_system: object) -> bytes:
    return des_system.encrypt(pad(data, 16))

def decrypt(cipher: bytes, des_system: object) -> bytes:
    return unpad(des_system.decrypt(cipher), 16) #try it without unpadding!

if __name__ == '__main__':
    main()