from srcs import read

def rewrite_log():
    all_log = read.read_file()
    # all_log = read.read_stdin()
    start = all_log[0][0]
    for step in all_log:
        step[0] = step[0] - start
        print("{0:<8}{1} {2}".format(step[0], step[1], step[2]))

rewrite_log()
