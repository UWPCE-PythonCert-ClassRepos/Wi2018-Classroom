#!/usr/bin/env python3

def rot13(cleartext):
    """Return ROT13 ciphertext"""
    aord = ord("a")
    Aord = ord("A")
    retstr = ""
    for char in cleartext:
        if (char >= "a" and char <= "z"):
            ordchar = ord(char) - aord
            ordchar = (ordchar + 13) % 26
            ordchar += aord
            char = chr(ordchar)
        elif (char >= "A" and char <= "Z"):
            ordchar = ord(char) - Aord
            ordchar = (ordchar + 13) % 26
            ordchar += Aord
            char = chr(ordchar)
        retstr += char
    return retstr

if __name__ == '__main__':
    assert(rot13("cleartext") == "pyrnegrkg") # known ciphertext

    tests = ("cleartext",
             "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    for test in tests:
        assert(rot13(test) != test)
        assert(rot13(rot13(test)) == test)

    print("Passed.")
