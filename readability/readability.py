# My reference: https://docs.python.org/3/howto/regex.html

from sys import exit
import re


def main():
    # get text
    while True:
        try:
            text = str(input("Text: "))
        except TypeError:
            print("Please enter a string of words.")
        else:
            if len(text) < 1:
                print("Please enter a string of words.")
            else:
                l = get_l(text)
                s = get_s(text)
                level = round(0.0588 * l - 0.296 * s - 15.8)
                if level > 16:
                    level = "16+"
                elif level < 1:
                    level = "Before Grade 1"
                print(f"Grade {level}")
                exit(0)

    # get letters/100 words


def get_l(txt):
    letter_re = re.compile("[a-zA-Z]")
    words_re = re.compile("\\S+")
    words = len(words_re.findall(txt))
    letters = len(letter_re.findall(txt))
    return letters / (words / 100)

    # get sentences/100 words


def get_s(txt):
    words_re = re.compile("\\S+")
    sentences_re = re.compile(r"[.?!]")
    words = len(words_re.findall(txt))
    sentences = len(sentences_re.findall(txt))
    return sentences / (words / 100)


main()
