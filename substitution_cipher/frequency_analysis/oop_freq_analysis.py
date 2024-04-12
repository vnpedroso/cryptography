from string import ascii_lowercase
from operator import itemgetter

class FreqAnalysisAttack():
    def __init__(self):
        self.alphabet = ascii_lowercase
        self.remainder_cipher_chars = ascii_lowercase
        self.remainder_alphabet = ascii_lowercase
        self.cipher = ""
        self.freq = {}
        self.mappings = {}
        self.key = {}
        self.message = ""
        self.expected_freq = {
            'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
            'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403, 
            'm': 0.0241,'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 
            's': 0.0633, 't': 0.0906,'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
            'y': 0.0197, 'z': 0.0007
        }

    def load_cipher(self, path: str) -> None:
        with open(path, 'r') as file:
            self.cipher = file.read().lower()
        return None

    def calculate_freq(self) -> None:
        for char in self.alphabet:
            self.freq[char] = 0

        cipher_total = 0

        for char in self.cipher:
            if char in self.freq.keys():
                self.freq[char] += 1
                cipher_total += 1

        for k, v in self.freq.items():
            self.freq[k] = round(v / cipher_total, 4)
        return None


    def match_frequencies(self) -> None:
        for outer_char in self.alphabet:
            mappings = {}
            for inner_char in self.alphabet:
                mappings[inner_char] = round(
                    abs(self.freq[outer_char] - self.expected_freq[inner_char]),
                    4
                )
            self.mappings[outer_char] = sorted(mappings.items(), key=itemgetter(1))
        return None

    def guess_key(self) -> None:
        for outer_char in self.remainder_cipher_chars:
            for inner_char, _ in self.mappings[outer_char]:
                if inner_char in self.remainder_alphabet:
                    self.key[outer_char] = inner_char
                    self.remainder_alphabet = self.remainder_alphabet.replace(inner_char, '')
                    break
        return None

    def manual_key_mapping(self, cipher_char: str, char: str) -> None:
        cipher_char = cipher_char.lower()
        char = char.lower()
        if cipher_char not in (self.remainder_cipher_chars or self.remainder_alphabet):
            raise ValueError(f"key mapping error: {cipher_char} :: {char}")
        self.key[cipher_char] = char
        self.remainder_alphabet = self.remainder_alphabet.replace(char, '')
        self.remainder_cipher_chars = self.remainder_cipher_chars.replace(cipher_char, '')
        return None

    def display(self, d: dict) -> None:
        line_cnt = 0
        for k,v in d.items():
            print(k, ':', v, '\t', end='')
            if line_cnt % 3 == 2:
                print()
            line_cnt += 1
        print('\n'*2)
        return None

    def cipher_message_comparison(self) -> None:
        message_lines = self.message.splitlines()
        cipher_lines = self.cipher.splitlines()
        print()
        for i in range(len(message_lines)):
            print('M: ', message_lines[i])
            print('C: ', cipher_lines[i], '\n')
        return None


    def decrypt(self) -> None:
        for char in self.cipher:
            if char in self.key.keys():
                self.message += self.key[char]
            else:
                self.message += char
        return None

if __name__ == "__main__":

    attack = FreqAnalysisAttack()
    attack.load_cipher(path = "./cryptography/frequency_analysis/cipher.txt")
    attack.calculate_freq()
    attack.match_frequencies()

    #for crytography/substitution_cipher/frequency_analysis/cipher.txt

    # attack.manual_key_mapping(cipher_char="z",char="y")
    # attack.manual_key_mapping(cipher_char="p",char="o")
    # attack.manual_key_mapping(cipher_char="m",char="u")
    # attack.manual_key_mapping(cipher_char="y",char="w")
    # attack.manual_key_mapping(cipher_char="g",char="t")
    # attack.manual_key_mapping(cipher_char="n",char="r")
    # attack.manual_key_mapping(cipher_char="c",char="n")
    # attack.manual_key_mapping(cipher_char="f",char="v")
    # attack.manual_key_mapping(cipher_char="a",char="k")
    # attack.manual_key_mapping(cipher_char="u",char="c")
    # attack.manual_key_mapping(cipher_char="t",char="g")
    # attack.manual_key_mapping(cipher_char="e",char="a")
    # attack.manual_key_mapping(cipher_char="x",char="h")
    # attack.manual_key_mapping(cipher_char="v",char="i")
    # attack.manual_key_mapping(cipher_char="h",char="s")
    # attack.manual_key_mapping(cipher_char="d",char="p")
    # attack.manual_key_mapping(cipher_char="o",char="f")
    # attack.manual_key_mapping(cipher_char="j",char="m")

    attack.guess_key()

    message = attack.decrypt()

    attack.display(attack.freq)
    attack.display(attack.expected_freq)
    attack.display(attack.key)

    attack.cipher_message_comparison()
