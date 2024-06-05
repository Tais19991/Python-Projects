from morse_decoder_encoder import letters_to_morse_dict, MorseCodeEncrypt, MorseCodeDecrypt


def choose_options() -> str:
    """Ask user about encoding/decoding preferences, return 1 or 2 option"""
    user_option = input(f'\nChoose option\n'
                        f'1 - From English to Morse code;\n'
                        f'2 - From Morse code to English\n\n'
                        f'Enter number here: ').strip()

    if user_option != '1' and user_option != '2':
        print('\nPlease enter 1 or 2 option')
        return choose_options()
    else:
        return user_option


def morse_code_translator():
    """The main user-friendly flow for encoding/decoding from English to Morse and vice versa"""
    end_translation = False
    print('\n\nWelcome to Morse Code Translator!\n')

    while not end_translation:
        # run encryption or decryption according to user choice
        user_choice = choose_options()
        if user_choice == '1':
            user_text = input('\nEnter your text in English:\n')
            encrypted = MorseCodeEncrypt(user_text)
            morse_code = encrypted.run()
            if encrypted.excluded_symbols == '':
                print(f'\nYour encrypted text is: "{morse_code}"')
            else:
                print(f"\nSorry, I can't translate these symbols: '{encrypted.excluded_symbols}'\n\n"
                      f'Your encrypted text (untranslatable symbols are excluded): "{morse_code}"\n\n')

        elif user_choice == '2':
            print('\nFor better translation put "/" between potential words in your Morse code')
            code = input('\nEnter your Morse code:\n')
            decrypted = MorseCodeDecrypt(code)
            eng_text = decrypted.run()
            if decrypted.excluded_symbols == '':
                print(f'\nYour decrypted message is: "{eng_text}"')
            else:
                print(f"\nSorry, I can't translate these symbols: '{decrypted.excluded_symbols}'\n\n"
                      f'Your decrypted message is (untranslatable symbols are excluded): "{eng_text}"\n\n')

        # end of program handling
        repeat_translation = input('\nDo you want to start again? Y/n:').strip()
        if repeat_translation == 'Y' or repeat_translation == 'y':
            pass
        else:
            end_translation = True
            print('\nOk.See you later!')


if __name__ == '__main__':
    morse_code_translator()
