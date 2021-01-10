#!/usr/bin/env python3
import sys

def my_sed(from_word, to_word, file_name):
    fin = open(file_name, 'r')
    
    while True:
        line = fin.readline()
        if not line: break
        while from_word in line:
            idx = line.index(from_word)
            line = line[:idx] + to_word + line[idx+len(from_word):]
        
        print(line, end='')
    fin.close()
        


if __name__=="__main__":
    argument = sys.argv
    from_word = argument[1]
    to_word = argument[2]
    file_name = argument[3]
    my_sed(from_word, to_word, file_name)
