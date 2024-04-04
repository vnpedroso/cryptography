from os import system as os_system
from platform import system as ptf_system
from secrets import randbelow

def gen_key_stream(n: int) -> bytes: # n here must be the length of the message 
    assert isinstance(n, int), "argument n must be of INTEGER type"
    # generating a list of string representations of the binaries of these random integers
    return bytes([randbelow(256) for i in range(n)]) # this is our key!

def xor(key_stream: int | bytes, message: int | str | bytes) -> bytes:
    if isinstance(message, str):
        message = message.encode()
    if isinstance(message, int):
        message = message.to_bytes((message.bit_length() + 7) // 8, "big")
    if isinstance(message, bytes):
        pass
    else:
        raise TypeError("ERROR:: message parameter must be of type INT, STRING or BYTES")
    
    if isinstance(key_stream, int):
        key_stream = key_stream.to_bytes((key_stream.bit_length() + 7) //8, "big")
    if isinstance(key_stream, bytes):
        pass  
    else:
        raise TypeError("ERROR:: key_stream argument must be of type INT or BYTES")

    # the message cannot be longer than the key, otherwise we won't be able to encrypt all chars
    assert len(key_stream) >= len(message), "ERROR:: the key cannot be smaller then the message"

    return bytes([key_stream[i] ^ message[i] for i in range(len(key_stream))])

def clear_screen() -> None:
    if ptf_system() == "Windows":
        os_system("cls")
    else:
        os_system("clear")
    return None
