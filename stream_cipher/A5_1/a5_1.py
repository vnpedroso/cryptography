from pydantic import BaseModel, ValidationError, field_validator
from collections import deque
from typing import Any, Union

class Input(BaseModel):
    key: Union[int, str, bytes]
    message:  Union[int, str, bytes]

    @field_validator("key")
    @classmethod
    def validate_key(cls, key: Any) -> Any:
        if isinstance(key, str):
            key_bin = "".join(format(ord(char), "0b") for char in key)
            if len(key_bin) <= 64:
                raise ValidationError("ERROR:: string length of key parameter of type STR and have a minimum of 64 bits")
        if isinstance(key, int):
            key_bin = bin(key)
            if len(key_bin) <= 64:
                raise ValidationError("ERROR:: bit length of key parameter of type BYTES and have a minimum of 64 bits")
        if isinstance(key, bytes):
            key_bin = bin(int.from_bytes(key, "big"))
            if len(key_bin) <= 64:
                raise ValidationError("ERROR:: bit length of key parameter of type BYTES and have a minimum of 64 bits")
        return key_bin
    
    @field_validator("message")
    @classmethod
    def validate_message(cls, message: Any) -> Any:
        if isinstance(message, int):
            message = message.to_bytes((message.bit_length() + 7) // 8, "big")
        return message

class A5_1():

    def __init__(self, key) -> None:
        self.key = key[2:67]
        self.register1 = deque(self.key[:19], maxlen=19)
        self.register2 = deque(self.key[19:41], maxlen=22)
        self.register3 = deque(self.key[41:64], maxlen=23)

        return None
    
    def _election(self) -> None:
        return (
            (int(self.register1[8]) & int(self.register2[10])) | 
            (int(self.register1[8]) & int(self.register3[10])) | 
            (int(self.register2[10]) & int(self.register3[10]))
        )

    def _stepping(self, elected: int) -> None:
        if int(self.register1[-1]) == elected:
            temp1 = (
                int(self.register1[13]) ^ 
                int(self.register1[16]) ^ 
                int(self.register1[17]) ^ 
                int(self.register1[18])
            ) 
            self.register1.appendleft(str(temp1))

        if int(self.register2[-1]) == elected:
            temp2 = (
                int(self.register2[20]) ^ 
                int(self.register2[21]) 
            )
            self.register2.appendleft(str(temp2))

        if int(self.register3[-1]) == elected:
            temp3 = (
                int(self.register3[7]) ^ 
                int(self.register3[20]) ^ 
                int(self.register3[21]) ^ 
                int(self.register3[22])
            )
            self.register3.appendleft(str(temp3))
        
        return None

    def gen_encryption_byte(self) -> int:
        elected = self._election()
        self._stepping(elected)
        return int(self.register1[-1]) ^ int(self.register2[-1]) ^ int(self.register3[-1])
        
def xor(a51_stream: object, message: int | str | bytes) -> bytes:
    assert isinstance(a51_stream, A5_1), "ERROR:: key_stream argument must be of type A5_1"
    message_bits = "".join(format(ord(byte), "0b") for byte in message)
    return bytes([a51_stream.gen_encryption_byte() ^ int(message_bits[i]) for i in range(len(message_bits))])