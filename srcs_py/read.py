import sys
from srcs_py import const, err_flags, log
from srcs_py.parse import Parse

class Read():

    def read_stdin (error):
        instructions = []
        f = open(const.LOG_FILE, 'w')
        for line in sys.stdin:
            try:
                f.write(line)
                line = Parse.delete_escapesquence(line)
                if line == "":
                    break
                line = line.rstrip('\n').split(" ", 1)
                line.append(line[1].strip(" ").split(" ", 1)[1])
                line[1] = line[1].strip(" ").split(" ", 1)[0]
                line[0] = int(line[0])
                line[1] = int(line[1])
                instructions.append(line)
            except:
                error |= err_flags.Error.LOGFORMAT
                log.set_error_print_log(err_flags.Error.LOGFORMAT, line=line)
                pass
        f.close()
        return instructions

    def read_file (instructions, error):
        with open(const.READ_FILE) as f:
            for line in f:
                try:
                    line = line.rstrip('\n').split(" ", 2)
                    line[0] = int(line[0])
                    line[1] = int(line[1])
                    instructions.append(line)
                except:
                    error |= err_flags.Error.LOGFORMAT
                    log.set_error_print_log(err_flags.Error.LOGFORMAT, line=line)
                    pass
