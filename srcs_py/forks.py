from srcs_py import read, const, log

class Forks():

    def __init__(self, av):
        try:
            self.nb_of_pilos = int(av[1])
            self.time_to_die = int(av[2])
            self.time_to_eat = int(av[3])
            self.time_to_sleep = int(av[4])
        except:
            print("argv is required for checking death\n")
        self.max = self.nb_of_pilos
        self.instructions = read.read_stdin()
        self.forks = [0] * self.max
        # write in log file
        av.pop(0)
        log.print_start_log(av)
        self.print_instruction()

    def print_instruction (self):
        print(f'{const.GREEN}green = eating')
        print(f'{const.YELLOW}yellow = waiting a fork{const.RESET}\n')
        print(f'{"time(elapsed)":<10}')

    def check_simulation (self):
        time_start = self.instructions[0][0]
        time_prev = time_start
        for step in self.instructions:
            time = step[0]
            # when timestamp changed
            if (time != time_prev):
                self.print_forks(time_prev - time_start, time_prev)
                time_prev = time
            self.check_fork_status(time, step[1], step[2])
        self.print_forks(time_prev - time_start, time_prev)
        print()

        self.check_death()

        self.print_result()

    def print_forks(self, time_passed, time_prev):
        # print timepassed
        print("{1}({0:>8})".format(time_passed, str(time_prev)[-3:]), end=" ")
        if (self.forks[0] == self.max):
            print(f'{const.GRAY}', end="")
        i = 1
        for afork in self.forks:
            print(f'[{afork}]{const.RESET}', end=" ")
            # set philo color
            if (self.max != 1 and self.forks[i - 1] == i and
                ((i == self.max and self.forks[0] == i) or self.forks[i] == i)):
                print(f'{const.GREEN}', end="")
            elif ((i == self.max and self.forks[0] == i) or (i != self.max and self.forks[i] == i)):
                print(f'{const.YELLOW}', end="")
            print(f'{i}{const.RESET}', end=" ")
            i = i + 1
        if (self.forks[0] == self.max):
            print(f'[{self.forks[0]}]', end="")
        print()

    def print_result (self):
        print("[result]")
        for err_flag in const.FLAG_LST:
            print(f'{const.FLAG_INFO[err_flag]}: ' , end='')
            if const.ERROR_FLAGS & err_flag:
                print(f'{const.RED}[KO]{const.RESET}', end='\n')
            else:
                print(f'{const.GREEN}[OK]{const.RESET}', end='\n')
        print()
        print(f'see {const.LOG_FILE} for more details')

    def check_fork_status (self, time, philo_nb, action):
        right = philo_nb
        if (right == self.max):
            right = 0
        left = philo_nb - 1
        if (action == const.fork):
            if (self.forks[right] == philo_nb):
                if (self.forks[left] != 0):
                    log.set_error_print_log(const.ERR_FLAG_FORK, time=time, philo_nb=philo_nb)
                self.forks[left] = philo_nb
            else:
                if (self.forks[right] != 0):
                    log.set_error_print_log(const.ERR_FLAG_FORK, time=time, philo_nb=philo_nb)
                self.forks[right] = philo_nb
        elif (action == const.sleep):
            self.forks[right] = 0
            self.forks[left] = 0

    def check_death (self):
        philo_dead = self.instructions[-1][1]
        last_eat = self.instructions[0][0]
        num_fork = 0
        for step in self.instructions:
            time = step[0]
            philo_nb = step[1]
            action = step[2]
            if (last_eat - time >= self.time_to_die + 10 and action != const.died):
                log.set_error_print_log(const.ERR_FLAG_DEATH, philo_nb=philo_dead,
                time_exp=last_eat + self.time_to_die, time_act=time)
            if (time - last_eat < self.time_to_die and action == const.died):
                log.set_error_print_log(const.ERR_FLAG_DEATH, philo_nb=philo_dead,
                time_exp=last_eat + self.time_to_die, time_act=time)
            if (philo_nb == philo_dead and action == const.fork):
                num_fork = num_fork + 1
            if (num_fork == 2):
                last_eat = time
                num_fork = 0
        if (self.instructions[-1][2] != const.died or self.instructions[-2][2] == const.died):
            log.set_error_print_log(const.ERR_FLAG_EOS)