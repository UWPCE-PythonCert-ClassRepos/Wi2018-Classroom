#!/usr/local/opt/coreutils/libexec/gnubin/env python3
# rriehle 2018


def reverse_word(word):
    if word:
        return word[-1] + reverse_word(word[:-1])
    return ''


# def reverse_word(word):
#     return word[-1] + reverse_word(word[:-1]) if word else ''


def test_reverse_word():
    assert 'alone' == reverse_word('enola')


def main():
    print(reverse_word("enola"))


if __name__ == "__main__":
    main()
