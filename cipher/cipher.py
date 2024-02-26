from pprint import pprint
import inquirer

def main():
    # Get user input to encrypt or decrypt
    while True:
        getText = (input("Input a phrase: "))
        if len(getText) > 0:
            break

    # Get user key
    while True:
        getKey = (input("Input a key: "))
        if len(getKey) > 0:
            break 

    # encrypt or decrpyt?
    questions = [
        inquirer.List(
            "direction",
            message="Encrypt or decrypt?",
            choices=["Encrypt", "Decrypt"],
        ),
    ]

    answers = inquirer.prompt(questions)
    pprint(answers)

    get_direction = answers["direction"]

    # Encrypt or decrypt, based on user input
    match get_direction:
            case "Encrypt":
                encrypted = encrypt(getText, getKey)
                print(f'\nEncrypted: {encrypted}')
            case "Decrypt":
                decrypted = decrypt(getText, getKey)
                print(f'\nDecrypted: {decrypted}')


def vigenere(text, key, direction):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i, char in enumerate(text): 
        if not char.isalpha():
            output += char
        else:
            # Get alphabet index of character in text
            char_index = alpha.index(char.lower())
            # Get character in key
            key_char = key[i% len(key)] 
            # get amount of shift based on the alphabet index of the key character
            shift = alpha.index(key_char)
            # Use the shift to find the new letter in the alphabet
            output += alpha[(char_index + shift * direction) % len(alpha)]
    return output


def encrypt(text, key):
    return vigenere(text, key, 1)


def decrypt(text, key):
    return vigenere(text, key, -1)

main()


# Create text enryption
# alphabet
# check if alpha char
# get alph index of text char
# get alph index of key (divide by modulo key length)
# get shift = textindex + keyindex
# index + shift

# BONUS
# Make key finder using list of real words to test against -- print any possible key that generates all real words and the output!