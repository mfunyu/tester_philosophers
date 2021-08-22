#!/bin/bash

FILE = "./tests/log"

def read_file ():
    with open(FILE) as f:
        all_log = []
        for line in f:
            line = line.rstrip('\n').split(" ", 1)
            line[0] = int(line[0])
            all_log.append(line)
    return all_log

def main ():
    all_log = read_file()
    start = all_log[0][0]
    for step in all_log:
        step[0] = step[0] - start
        print("{0:<8}{1}".format(step[0], step[1]))

main ()
