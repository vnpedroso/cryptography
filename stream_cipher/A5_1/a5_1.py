from pydantic import BaseModel, ValidationError, field_validator
from typing import Any, Union

class Input(BaseModel):
    key: Union[int, str, bytes]

    @field_validator("key")
    @classmethod
    def validate_key(cls, key: Any) -> Any:
        if isinstance(key, int) and key.bit_length() <= 64:
            raise ValidationError("ERROR:: bit length of key parameter of type INT and have a minimum of 64 bits")
        elif isinstance(key, str) and len("".join(format(ord(char), "0b") for char in key)) <= 64:
            raise ValidationError("ERROR:: string length of key parameter of type STR and have a minimum of 64 bits")
        elif isinstance(key, bytes) and bin(int.from_bytes(key, "big")).bit_length() <= 64:
            raise ValidationError("ERROR:: bit length of key parameter of type BYTES and have a minimum of 64 bits")
        return key

class A5_1():

    def __init__(self, key):
    
        if isinstance(key, str):
            key_bin = "".join(format(ord(char), "0b") for char in key)
        if isinstance(key, int):
            key_bin = bin(key)
        if isinstance(key, bytes):
            key_bin = bin(int.from_bytes(key, "big"))

        self.key = key_bin[2:67]
        self.register1 = self.key[:19]
        self.register2 = self.key[19:41]
        self.register3 = self.key[41:64]


# if __name__ == "__main__":
#     data_input = Input(key=42231234343456789088)
#     a = A5_1(data_input.key)
#     print(a.key)
#     print(a.register1)
#     print(a.register2)
#     print(a.register3)