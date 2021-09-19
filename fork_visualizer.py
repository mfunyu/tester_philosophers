import sys
from srcs_py import const, read, log

fork="has taken a fork"
eat="is eating"
sleep="is sleeping"
think="is thinking"
died="died"

MAX = 0

def print_forks(forks, time_passed, time_prev):
    # print timepassed
    print("{1}({0:>8})".format(time_passed, str(time_prev)[-3:]), end=" ")
    i = 1
    for afork in forks:
        if (i == 1 and forks[0] == MAX):
            print("{0}".format(const.GRAY), end="")
        print("[{0}]".format(afork), end=" ")
        print("{0}".format(const.RESET), end="")
        if (forks[i - 1] == i and ((i == MAX and forks[0] == i) or forks[i] == i)):
            print("{0}".format(const.GREEN), end="")
        elif ((i == MAX and forks[0] == i) or (i != MAX and forks[i] == i)):
            print("{0}".format(const.YELLOW), end="")
        print(i, end=" ")
        print("{0}".format(const.RESET), end="")
        if (i == MAX and forks[0] == i):
            print("[{0}]".format(forks[0]), end=" ")
        i = i + 1
    print()

def change_fork_status (forks, step):
    philo_nb = step[1]
    action = step[2]
    right = philo_nb
    if (right == MAX):
        right = 0
    left = philo_nb - 1
    if (action == fork):
        if (forks[right] == philo_nb):
            if (forks[left] != 0):
                log.set_error_print_log(const.ERR_FLAG_FORK, time=step[0], philo_nb=philo_nb)
            forks[left] = philo_nb
        else:
            if (forks[right] != 0):
                log.set_error_print_log(const.ERR_FLAG_FORK, time=step[0], philo_nb=philo_nb)
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
            print_forks(forks, time_prev - time_start, time_prev)
            time_prev = time
        change_fork_status(forks, step)
    print_forks(forks, time_prev - time_start, time_prev)



def check_death (av, lst):
    try:
        nb_of_pilos = int(av[0])
        time_to_die = int(av[1])
        time_to_eat = int(av[2])
        time_to_sleep = int(av[3])
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
        if (last_eat - time >= time_to_die + 10 and action != died):
            log.set_error_print_log(const.ERR_FLAG_DEATH, philo_nb=philo_dead,
            time_exp=last_eat + time_to_die, time_act=time)
        if (time - last_eat < time_to_die and action == died):
            log.set_error_print_log(const.ERR_FLAG_DEATH, philo_nb=philo_dead,
            time_exp=last_eat + time_to_die, time_act=time)
        if (philo_nb == philo_dead and action == fork):
            num_fork = num_fork + 1
        if (num_fork == 2):
            last_eat = time
            num_fork = 0
    if (lst[-1][2] != died or lst[-2][2] == died):
        log.set_error_print_log(const.ERR_FLAG_EOS)

def print_result ():
    print("[result]")
    for err_flag in const.FLAG_LST:
        print(f'{const.FLAG_INFO[err_flag]}: ' , end='')
        if const.ERROR_FLAGS & err_flag:
            print(f'{const.RED}[KO]{const.RESET}', end='\n')
        else:
            print(f'{const.GREEN}[OK]{const.RESET}', end='\n')
    print()
    print(f'see {const.LOG_FILE} for more details')

def print_instruction ():
    print(f'{const.GREEN}green = eating\n\
{const.YELLOW}yellow = waiting a fork{const.RESET}\n')
    print(f'{"time(elapsed)":<10}')

def main ():
    global MAX
    av = sys.argv
    av.pop(0)
    log.print_start_log(av)
    if len(av) > 1:
        MAX = int(av[0])
    lst = read.read_stdin()
    # lst = read.read_file()
    print_instruction()
    try:
        visualize_forks(lst)
        check_death(av, lst)
        print_result()
    except:
        print(lst, f"{const.YELLOW}some error occured{const.RESET}")

if __name__ == "__main__":
    main()
