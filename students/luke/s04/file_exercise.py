#!/usr/bin/env python3

"""
https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/file_lab.html#exercise-file-lab

Write a little script that reads that file, and generates a list of all
the languages that have been used.
"""

infile = open("students.txt", 'r')

languages = {}

for line in infile:
    # split at :
    name, langs = line.split(':', 1)
    if name == 'Name':
        continue  # header
    for langent in langs.split(','):
        lang = langent.replace(' ', '').strip()
        if lang[:1].isupper():
            continue  # Nickname
        if not languages.get(lang):
            languages[lang] = []
        languages[lang].append(name)

for lang in languages.keys():
    print(f"{lang:>12}:\t{len(languages[lang]):4} students: {languages[lang]}")
