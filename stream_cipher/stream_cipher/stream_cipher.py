import os 
import platform

class KeyStream():
    def __init__(self, key=1) -> None:
        self.next = key

    def rand(self) -> object:
        # LCG - linear congruential generator --> x = (x + c) mod m
        # please do not choose poor params !!!
        self.next = (25612572 * self.next +  0) % (2**25 - 39)
        return self.next

    def gen_key_byte(self) -> int:
        return self.rand() % 256

def xor(key_stream: object, message: int | str | bytes) -> bytes:
    if isinstance(message, str):
        message = message.encode()
    if isinstance(message, int):
        message = message.to_bytes((message.bit_length() + 7) // 8, "big")
    if isinstance(message, bytes):
        pass
    else:
        raise TypeError("ERROR:: message parameter must be of type INT, STRING or BYTES")
    
    assert isinstance(key_stream, KeyStream), "ERROR:: key_stream argument must be of type KeyStream"

    return bytes([key_stream.gen_key_byte() ^ message[i] for i in range(len(message))])

def clear_screen() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    return None