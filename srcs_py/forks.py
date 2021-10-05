from os import defpath
import sys
from srcs_py import const, log, err_flags

class Forks():

    def __init__(self, av, readfromstdin):
        try:
            self.nb_of_pilos = int(av[1])
            self.time_to_die = int(av[2])
            self.time_to_eat = int(av[3])
            self.time_to_sleep = int(av[4])
            try:
                self.nb_of_eat = int(av[5])
            except:
                self.nb_of_eat = -1
        except:
            print("argv is required for checking death\n")
        self.max = self.nb_of_pilos
        self.error = err_flags.Error(0)
        self.instructions = []
        log.print_start_log(av)
        print("Start loading instructions ...")
        if readfromstdin:
            self.read_stdin()
        else:
            self.read_file()
        self.forks = [0] * self.max
        # write in log file
        av.pop(0)

    def read_stdin (self):
        f = open(const.LOG_FILE, 'w')
        for line in sys.stdin:
            try:
                f.write(line)
                line = line.rstrip('\n').split(" ", 1)
                line.append(line[1].strip(" ").split(" ", 1)[1])
                line[1] = line[1].strip(" ").split(" ", 1)[0]
                line[0] = int(line[0])
                line[1] = int(line[1])
                self.instructions.append(line)
            except:
                self.error |= err_flags.Error.LOGFORMAT
                log.set_error_print_log(err_flags.Error.LOGFORMAT, line=line)
                pass
        f.close()

    def read_file (self):
        with open(const.READ_FILE) as f:
            for line in f:
                try:
                    line = line.rstrip('\n').split(" ", 2)
                    line[0] = int(line[0])
                    line[1] = int(line[1])
                    self.instructions.append(line)
                except:
                    self.error |= err_flags.Error.LOGFORMAT
                    log.set_error_print_log(err_flags.Error.LOGFORMAT, line=line)
                    pass

    def print_instruction (self):
        print(f'{const.GREEN}green = eating')
        print(f'{const.YELLOW}yellow = waiting a fork{const.RESET}\n')
        print(f'{"time(elapsed)":<10}')

    def advanced_tests (self):
        print("Start running tests ...")
        self.print_instruction()
        self.check_actionlength()
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
        if self.nb_of_eat == -1:
            self.check_death()
        else:
            self.check_nb_eat()
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
        for err_flag in err_flags.Error:
            if self.nb_of_eat == -1 and err_flag == err_flags.Error.NBEAT:
                continue
            if self.nb_of_eat != -1 and err_flag == err_flags.Error.DEATH:
                continue
            print(f'{err_flags.Error.flag2str(err_flag)}: ' , end='')
            if self.error & err_flag:
                print(f'{const.RED}[KO]{const.RESET}', end='\n')
            else:
                print(f'{const.GREEN}[OK]{const.RESET}', end='\n')
        print()
        print(f'see {const.LOG_FILE} for philo output')
        print(f'see {const.RESULTS_FILE} for more details')

    def check_fork_status (self, time, philo_nb, action):
        right = philo_nb
        if (right == self.max):
            right = 0
        left = philo_nb - 1
        if (action == const.fork):
            if (self.forks[right] == philo_nb):
                if (self.forks[left] != 0):
                    self.error |= err_flags.Error.FORK
                    log.set_error_print_log(err_flags.Error.FORK, time=time, philo_nb=philo_nb)
                self.forks[left] = philo_nb
            else:
                if (self.forks[right] != 0):
                    self.error |= err_flags.Error.FORK
                    log.set_error_print_log(err_flags.Error.FORK, time=time, philo_nb=philo_nb)
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
                self.error |= err_flags.Error.DEATH
                log.set_error_print_log(err_flags.Error.DEATH, philo_nb=philo_dead,
                time_exp=last_eat + self.time_to_die, time_act=time)
            if (time - last_eat < self.time_to_die and action == const.died):
                self.error |= err_flags.Error.DEATH
                log.set_error_print_log(err_flags.Error.DEATH, philo_nb=philo_dead,
                time_exp=last_eat + self.time_to_die, time_act=time)
            if (philo_nb == philo_dead and action == const.fork):
                num_fork = num_fork + 1
            if (num_fork == 2):
                last_eat = time
                num_fork = 0
        if (self.instructions[-1][2] != const.died or self.instructions[-2][2] == const.died):
            self.error |= err_flags.Error.EOS
            log.set_error_print_log(err_flags.Error.EOS)

    def check_nb_eat(self):
        cnt = [0] * (self.nb_of_pilos + 1)
        exceed = 0
        for step in self.instructions:
            if step[2] == const.eat:
                cnt[step[1]] = cnt[step[1]] + 1
        for i in range(1, self.nb_of_pilos + 1):
            if cnt[i] < self.nb_of_eat:
                self.error |= err_flags.Error.NBEAT
                log.set_error_print_log(err_flags.Error.NBEAT, philo_nb=step[1], eat=cnt[i])
            if cnt[i] > self.nb_of_eat:
                exceed = exceed + 1
        if exceed == self.nb_of_pilos:
            self.error |= err_flags.Error.NBEAT
            log.set_error_print_log(err_flags.Error.NBEAT, philo_nb=step[1], eat=cnt[1])

    def check_actionlength(self):
        dict_tmp = {"time_eatst":0, "time_sleepst":0}
        lst = [dict_tmp.copy() for i in range(self.nb_of_pilos)]
        for step in self.instructions:
            lst_i = lst[step[1] - 1]
            time_now = step[0]
            action = step[2]
            if action == const.eat:
                lst_i["time_eatst"] = time_now
            elif action == const.sleep:
                diff = time_now - lst_i["time_eatst"] - self.time_to_eat
                if diff > const.ACCEPTABLE_DIFF:
                    self.error |= err_flags.Error.TIME
                    log.set_error_print_log(err_flags.Error.TIME, time=time_now,
                        philo_nb=step[1], action="ate", diff=diff)
                lst_i["time_sleepst"] = time_now
            elif action == const.think:
                diff = time_now - lst_i["time_sleepst"] - self.time_to_sleep
                if diff > const.ACCEPTABLE_DIFF:
                    self.error |= err_flags.Error.TIME
                    log.set_error_print_log(err_flags.Error.TIME, time=time_now,
                        philo_nb=step[1], action="slept", diff=diff)
