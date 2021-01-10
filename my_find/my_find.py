#!/usr/bin/env python3
import os
import sys

def search_file(dir_, suffix):
    files = os.listdir(dir_)
    for file in files:
        file_name = os.path.join(dir_, file)
        if os.path.isdir(file_name):
            search_file(file_name, suffix)

        _, ext = os.path.splitext(file_name)
        if ext[1:] == suffix:
            print(file_name)


if __name__=="__main__":
    argument = sys.argv
    dir_ = argument[1]
    suffix = argument[2]
    search_file(dir_, suffix)
    
