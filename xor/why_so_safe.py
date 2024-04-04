from xor.xor import (
    gen_key_stream,
    xor
)

opt1 = "start attack"
opt1 = opt1.encode()
key = gen_key_stream(n=len(opt1))
cipher = xor(key_stream=key,message=opt1)

print(f"message: {opt1}\n + \noriginal_key: {key} \n= cipher: {cipher}\n\n")

opt2 = "don't attack"
opt2 = opt2.encode()
guessed_key = xor(opt2, cipher)
guessed_msg = xor(cipher, guessed_key)

print(f"cipher: {cipher}\n + \nguessed_key: {key} \n= guessed_msg: {guessed_msg}")



