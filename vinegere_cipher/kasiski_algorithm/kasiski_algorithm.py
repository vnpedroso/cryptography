from collections import Counter
from string import ascii_lowercase
import re

class KasiskiAlgorithm():
    def __init__(self, cipher: str):
        self.cipher = cipher
        self.clean_cipher = "".join([char.lower() for char in cipher if char.isalpha()])
        self.topn_prime_factors = []
        self.factor_synched_substrings = {}
        self.estimated_key_letters_per_factor = {}
        self.expected_freq = {
            'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
            'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403, 
            'm': 0.0241,'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599, 
            's': 0.0633, 't': 0.0906,'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
            'y': 0.0197, 'z': 0.0007
        }

    def _prime_factorization(self, n: int) -> list[int]:
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def get_topn_prime_factors(self, topn: int) -> None:
        sequences = re.findall(r'(?=(\w{6,})).', self.cipher)
        sequence_counts = Counter(sequences)

        frequent_sequences = {seq: count for seq, count in sequence_counts.items() if count > 1}

        distances = {}
        for seq in frequent_sequences:
            indices = [m.start() for m in re.finditer(seq, self.cipher)]
            distances[seq] = [indices[i] - indices[i - 1] for i in range(1, len(indices))]

        all_distances = [dist for sublist in distances.values() for dist in sublist]
        all_prime_factors = [factor for dist in all_distances for factor in self._prime_factorization(dist)]
        prime_factor_counts = Counter(all_prime_factors)

        self.topn_prime_factors = prime_factor_counts.most_common(topn)

        return None

    def get_factor_synched_substrings(self) -> None:
        assert self.topn_prime_factors, "topn_prime_factors not calculated yet. Call get_topn_prime_factors() first."

        for factor, _ in [tup for tup in self.topn_prime_factors]:
            self.factor_synched_substrings[factor] = []
            for indx in range(factor):
                substring = ""
                for n, char in enumerate(self.clean_cipher):
                    if (n + indx) % factor == 0:
                        substring += char
                self.factor_synched_substrings[factor].append(substring)

        for i in self.factor_synched_substrings:
            assert len(self.factor_synched_substrings[i]) == i, "every factor (n) should have (n) substrings"

        return None
    
    def get_estimated_key_letters_per_factor(self, guess_per_index: int = 3) -> None:
        assert self.factor_synched_substrings, "factor_synched_substrings not calculated yet. Call get_factor_synched_substrings() first."
        
        for factor, substring_list in self.factor_synched_substrings.items():
            self.estimated_key_letters_per_factor[factor] = {}
            for indx, substring in enumerate(substring_list):
                guess = {}
                for letter in ascii_lowercase:
                    vinegere_string = ""
                    for char in substring:
                        vinegere_index = (substring.find(char) + ascii_lowercase.find(letter)) % len(ascii_lowercase)
                        vinegere_string += ascii_lowercase[vinegere_index]
                    vinegere_string_freq = Counter(vinegere_string) 
                    chi_square_freq = sum(
                        [abs(
                            (vinegere_string_freq[grapheme] / len(substring)) - self.expected_freq[grapheme]
                            )**2 / self.expected_freq[grapheme]
                          for grapheme in ascii_lowercase
                        ]
                    )
                    guess[letter] = chi_square_freq
                top_x_guesses = sorted(guess, key=guess.get)[:guess_per_index]
                self.estimated_key_letters_per_factor[factor][indx] = top_x_guesses
            
        for k1, v1 in self.estimated_key_letters_per_factor.items():
            for k2, v2 in v1.items():
                print(f"factor {k1}\t index {k2}\t guesses = {v2}")

        return None
            