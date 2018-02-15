# File lab

import os
from pathlib import Path
def get_files(dir="."):
    for i,v in enumerate(os.listdir(dir)):
        print(f"File {i+1}. {os.path.abspath(v)}")

get_files()

def copy_file(fin,fout=None):
    """
    Copy a file from one location to another. default to userhome if no output location is provided.
    :param fin:
    :param fout:
    :return:
    """
    if fout is None:
        fout=Path.joinpath(Path.home(),os.path.basename(fin))

    with open(fin,'rb') as f:
        data=f.read()
    with open(fout,'wb') as w:
        w.write(data)
    print(f"File copied to {fout}")

copy_file("dict_lab.py")

