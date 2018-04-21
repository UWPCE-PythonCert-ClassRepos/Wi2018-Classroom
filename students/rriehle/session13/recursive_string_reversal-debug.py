#!/usr/local/opt/coreutils/libexec/gnubin/env python3


def reverse_word(word):
    if word:
        print("word is {}, word[-1] is {}, word[:-1] is {}".format(
            word, word[-1], word[:-1],
        ))
        return word[-1] + reverse_word(word[:-1])
    else:
        print("word is empty, returning empty string")
        return ''


def main():
    print(reverse_word("Enola"))


if __name__ == "__main__":
    main()
