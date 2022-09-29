from morse_alphabet import MORSE_CODE_ENCODE_DICT, MORSE_CODE_DECODE_DICT


def encode(message, code_dict):
    """Encode english letters and digits to Norse code.
    Unknown for converter characters remain in original representation at the original place."""
    converted_message = ""
    unknown_symbols = []
    for symbol in message:
        try:
            converted_message += code_dict[symbol] + " "
        except KeyError:
            if symbol == " ":
                converted_message += "  "
            else:
                converted_message += symbol
                unknown_symbols.append(symbol)

    if unknown_symbols:
        print(f"The converter did not recognize the following characters: {' '.join(unknown_symbols)}\n"
              f"These characters are left unencoded in your message.")

    return converted_message


def decode(message, code_dict):
    """Decode from Morse code to english letters and digits.
    NOTE: for correct work each letter or digit in the Morse code representation must be separated
    by one space and two spaces must be used to separate whole words.
    Unknown for converter characters remain in original representation at the original place"""
    converted_message = ""
    unknown_symbols = []

    separated_words_list = message.split("  ")

    for word in separated_words_list:
        for symbol in word.split(" "):
            try:
                converted_message += code_dict[symbol]
            except KeyError:
                converted_message += symbol
                unknown_symbols.append(symbol)
        converted_message += " "

    if unknown_symbols:
        print(f"The converter did not recognize the following characters: {' '.join(unknown_symbols)}\n"
              f"These characters are left unencoded in your message.")

    return converted_message


def try_again():
    again = input("Would you like to try again? y/n: ").lower()
    while again not in ("y", "n"):
        again = input("Incorrect answer.\nWould you like to try again? y/n: ").lower()

    if again == "y":
        return True
    else:
        print("See you next time.")
        return False


def main():
    print("WELCOME TO THE MORSE CODE CONVERTER.")
    app_works = True
    while app_works:
        mode = input("Input 'e' to encode or 'd' to decode your message. e/d?: ").lower()

        if mode == 'e':
            print("\nENCODING MODE IS ACTIVATED")
            original_message = input("Input your message:\n").upper()
            converted_message = encode(original_message, MORSE_CODE_ENCODE_DICT)
            print(f"\nYour encoded message is:\n{converted_message}\n")
            app_works = try_again()

        elif mode == "d":
            print("\nDECODING MODE IS ACTIVATED")
            print(
                "PLEASE NOTE: for correct work each letter or digit in the Morse code\n"
                "representation must be separated by one space and two spaces must be used to separate whole words\n")
            original_message = input(
                "Input your message (use '0' for short signals and '1' for long):\n").upper()
            converted_message = decode(original_message, MORSE_CODE_DECODE_DICT)
            print(f"\nYour encoded message is:\n{converted_message}\n")
            app_works = try_again()

        else:
            print("Incorrect answer.\n")


if __name__ == '__main__':
    main()
