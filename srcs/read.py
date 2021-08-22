import sys

from srcs import const

def read_file ():
    with open(const.FILE) as f:
        lst = []
        for line in f:
            line = line.rstrip('\n').split(" ", 2)
            line[0] = int(line[0])
            line[1] = int(line[1])
            lst.append(line)
    return lst

def read_stdin ():
    input = []
    for line in sys.stdin:
        line = line.rstrip('\n').split(" ", 1)
        line.append(line[1].strip(" ").split(" ", 1)[1])
        line[1] = line[1].strip(" ").split(" ", 1)[0]
        line[0] = int(line[0])
        line[1] = int(line[1])
        input.append(line)
    return input
