#!/usr/bin/env python3
import sys

def main(file):
    costs = []
    fin = open(file, 'r')
    while True:
        N = fin.readline().strip()
        works = fin.readline().strip().split(',')
        if not N: break

        works = [int(i) for i in works]
        
        sum = 0

        for i in range(int(N)):
            max_num = max(works)
            works[works.index(max_num)] -= 1
        
        for work in works:
            sum += work**2
        
        costs.append(sum)

    fin.close()

    for cost in costs:
        print(cost)


if __name__=="__main__":
    argument = sys.argv
    main(argument[1])
