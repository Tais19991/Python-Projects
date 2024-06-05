from typing import Tuple

letters_to_morse_dict = {"a": '._', 'b': '_...', 'c': '_._.',
                         'd': '_..', 'e': '.', 'f': '.._.',
                         'g': '__.', 'h': '....', 'i': '..',
                         'j': '.___', 'k': '_._', 'l': '._..',
                         'm': '__', 'n': '_.', 'o': '___',
                         'p': '.__.', 'q': '__._', 'r': '._.',
                         's': '...', 't': '_', 'u': '.._',
                         'v': '..._', 'w': '.__', 'x': '_.._',
                         'y': '_.__', 'z': '__..', '1': '.____',
                         '2': '..___', '3': '...__', '4': '...._',
                         '5': '.....', '6': '_....', '7': '__...',
                         '8': '___..', '9': '____.', '0': '_____',
                         ' ': '/', '.': '.-.-.-', ',': '--..--',
                         ':': '---...', ';': '-.-.-.', '?': '..--..',
                         '-': '-....-', '_': '..--.-', '(': '-.--.',
                         ')': '-.--.-', "'": ".----.", '=': '-...-',
                         '+': '.-.-.', '/': "-..-.", '@': ".--.-.",
                         'Ñ': '--.--'}


class MorseCodeEncrypt:
    """Class for Translation text from English to International Morse Code"""

    def __init__(self, text_for_translation: str) -> None:
        self.morse_code = ''
        self.excluded_symbols = ''
        self.text_for_translation = text_for_translation.strip()
        self.letters_to_translate = [char for char in self.text_for_translation.lower()]
        self.dict_for_translation = letters_to_morse_dict

    def __repr__(self) -> str:
        return f'TranslateToMorseCode({self.dict_for_translation}, {self.text_for_translation})'

    def run(self) -> str:
        """Take list of English letters and return translated MorseCode as a str"""
        prev_char = None
        for letter in self.letters_to_translate:
            try:
                prev_char = letter
                self.morse_code += self.dict_for_translation[letter] + ' '

            except KeyError:
                self.excluded_symbols += prev_char
                pass

        return self.morse_code


class MorseCodeDecrypt:
    """Class for Translation Morse Code to English text"""

    def __init__(self, code_for_decryption: str) -> None:
        self.decrypted_text = ''
        self.excluded_symbols = ''
        self.code_for_decryption = code_for_decryption
        self.dict_for_decryption = {v: k for k, v in letters_to_morse_dict.items()}
        self.list_for_decryption = self.code_for_decryption.strip().split()

    def __repr__(self) -> str:
        return f'TranslateToMorseCode({self.dict_for_decryption}, {self.code_for_decryption})'

    def run(self) -> str:
        """Take list of Morse code 'letters' and return translated English text as a str"""
        prev_code = None
        for code in self.list_for_decryption:
            try:
                prev_code = code
                self.decrypted_text += self.dict_for_decryption[code]

            except KeyError:
                self.excluded_symbols += prev_code
                self.decrypted_text += '#'
                pass

        return self.decrypted_text
