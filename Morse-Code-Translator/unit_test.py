import unittest
from morse_decoder_encoder import MorseCodeDecrypt, MorseCodeEncrypt


class TestMorseTranslation(unittest.TestCase):

    def test_decode_encode(self):
        """decode and encode normal chars"""
        phrase = 'qwerty 123456789 cat and mouse'
        encoded_text = MorseCodeEncrypt(phrase).run()
        decoded_text = MorseCodeDecrypt(encoded_text).run()
        self.assertEqual(phrase, decoded_text)

    def test_unexpected_symbols(self):
        """find and exclude wrong symbols from given str"""
        # from english str
        phrase1 = '$ cat $ and mou#se #'
        encrypting = MorseCodeEncrypt(phrase1)
        encrypting.run()
        wrong_char = encrypting.excluded_symbols
        self.assertEqual(wrong_char, '$$##')

        # from morse str
        phrase2 = '/ _._. ._ _ / ._ _. _.. / __ ___ .._ ...___...___ . /'
        decrypting = MorseCodeDecrypt(phrase2)
        decrypting.run()
        wrong_code = decrypting.excluded_symbols
        self.assertEqual(wrong_code, '...___...___')


if __name__ == '__main__':
    unittest.main()
