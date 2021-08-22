import sys
import logging
fork="has taken a fork"
eat="is eating"
sleep="is sleeping"
think="is thinking"
died="died"


THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
GRAY="\033[38;5;240m"
RESET="\033[m"

ERR_FLAG_FORK = 0b1
ERR_FLAG_DEATH = 0b10
ERR_FLAG_EOS = 0b100
ERROR_FLAGS = 0
FLAG_LST = [ERR_FLAG_FORK, ERR_FLAG_DEATH, ERR_FLAG_EOS]

MAX = 0
LOG_FILE='./tests/tester_log'

logger = logging.getLogger("logger")    #logger名loggerを取得
logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで
#handlerを作成
handler = logging.FileHandler(filename=LOG_FILE)
handler.setFormatter(logging.Formatter("%(filename)8s: %(message)s"))
logger.addHandler(handler)

def read_file ():
    global MAX
    with open("./tests/log") as f:
        lst = []
        for line in f:
            line = line.rstrip('\n').split(" ", 2)
            line[0] = int(line[0])
            line[1] = int(line[1])
            if (line[1] > MAX):
                MAX = line[1]
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

def print_forks(forks, time_passed):
    # print timepassed
    print("{0:<10}".format(time_passed), end=" ")
    i = 1
    for afork in forks:
        if (i == 1 and forks[0] == MAX):
            print("{0}".format(GRAY), end="")
        print("[{0}]".format(afork), end=" ")
        print("{0}".format(RESET), end="")
        if (forks[i - 1] == i and ((i == MAX and forks[0] == i) or forks[i] == i)):
            print("{0}".format(GREEN), end="")
        elif ((i == MAX and forks[0] == i) or (i != MAX and forks[i] == i)):
            print("{0}".format(YELLOW), end="")
        print(i, end=" ")
        print("{0}".format(RESET), end="")
        if (i == MAX and forks[0] == i):
            print("[{0}]".format(forks[0]), end=" ")
        i = i + 1
    print()

def change_fork_status (forks, step):
    global ERROR_FLAGS
    philo_nb = step[1]
    action = step[2]
    right = philo_nb
    if (right == MAX):
        right = 0
    left = philo_nb - 1
    if (action == fork):
        if (forks[right] == philo_nb):
            if (forks[left] != 0):
                logger.debug(f"the fork philosopher {philo_nb} grabbed was not yet released")
                ERROR_FLAGS |= ERR_FLAG_FORK
            forks[left] = philo_nb
        else:
            if (forks[right] != 0):
                logger.debug(f"the fork philosopher {philo_nb} grabbed was not yet released")
                ERROR_FLAGS |= ERR_FLAG_FORK
            forks[right] = philo_nb
    elif (action == sleep):
        forks[right] = 0
        forks[left] = 0

def visualize_forks (lst):
    forks = [0] * MAX
    time_start = lst[0][0]
    time_prev = time_start
    for step in lst:
        time = step[0]
        # when timestamp changed
        if (time != time_prev):
            print_forks(forks, time_prev - time_start)
            time_prev = time
        change_fork_status(forks, step)


def check_death (av, lst):
    global ERROR_FLAGS
    try:
        nb_of_pilos = int(av[1])
        time_to_die = int(av[2])
        time_to_eat = int(av[3])
        time_to_sleep = int(av[4])
    except:
        print("argv is required for checking death\n")
        return (0)
    philo_dead = lst[-1][1]
    last_eat = lst[0][0]
    num_fork = 0
    for step in lst:
        time = step[0]
        philo_nb = step[1]
        action = step[2]
        if (last_eat - time >= lst[0][0] + time_to_die and action != died):
            logger.debug(f"the philosopher {philo_dead} lived too long.\n\
the philosopher {philo_dead} was supposed to die at {lst[0][0] + time_to_die}, \
but died at {time}; {lst[0][0] + time_to_die - time}ms late")
            ERROR_FLAGS |= ERR_FLAG_DEATH
        if (time - last_eat < time_to_die and action == died):
            logger.debug(f"the philosopher {philo_dead} died too early.\n\
the philosopher {philo_dead} was supposed to die at {lst[0][0] + time_to_die}, \
but died at {time}; {lst[0][0] + time_to_die - time}ms early")
            ERROR_FLAGS |= ERR_FLAG_DEATH
        if (philo_nb == philo_dead and action == fork):
            num_fork = num_fork + 1
        if (num_fork == 2):
            last_eat = time
            num_fork = 0
    if (lst[-1][2] != died):
        logger.debug(f"operation after death")
        ERROR_FLAGS |= ERR_FLAG_EOS

def print_result ():
    print("result: ", end=" ")
    for err_flag in FLAG_LST:
        if ERROR_FLAGS & err_flag:
            print(f'{RED}[KO]{RESET}', end=" ")
        else:
            print(f'{GREEN}[OK]{RESET}', end=" ")
    print()
    print(f'see {LOG_FILE} for more details')

def print_instruction ():
    print(f'{GREEN}green = eating\n{YELLOW}yellow = waiting a fork{RESET}\n')
    print(f'{"time_passed":<10}')

def main ():
    global MAX
    av = sys.argv
    if len(av) > 1:
        MAX = int(av[1])
    lst = read_stdin()
    # lst = read_file()
    print_instruction()
    visualize_forks(lst)
    check_death(av, lst)
    print_result()

main()
