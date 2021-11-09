from srcs_py import const, err_flags

class Print():

    def print_instruction ():
        print(f'{const.GREEN}green = eating')
        print(f'{const.YELLOW}yellow = waiting a fork{const.RESET}')
        print(f'{const.RED}red = dead{const.RESET}')
        print()
        print(f'{"time(elapsed)":<10}')

    def print_result (nb_of_eat, error):
        print("[result]")
        for err_flag in err_flags.Error:
            if nb_of_eat == -1 and err_flag == err_flags.Error.NBEAT:
                continue
            if nb_of_eat != -1 and err_flag == err_flags.Error.DEATH:
                continue
            print(f'{err_flags.Error.flag2str(err_flag)}: ' , end='')
            if error & err_flag:
                print(f'{const.RED}[KO]{const.RESET}', end='\n')
            else:
                print(f'{const.GREEN}[OK]{const.RESET}', end='\n')
        print()
        print(f'see {const.LOG_FILE} for philo output')
        print(f'see {const.RESULTS_FILE} for more details')


    def print_forks(forks, time_start, time_prev, philo_dead, nb_of_pilos):
        # print timepassed
        time_passed = time_prev - time_start
        print("{1}({0:>8})".format(time_passed, str(time_prev)[-3:]), end=" ")
        if (forks[0] == nb_of_pilos):
            print(f'{const.GRAY}', end="")
        i = 1
        for afork in forks:
            print(f'[{afork}]{const.RESET}', end=" ")
            # set philo color
            if (i == philo_dead):
                print(f'{const.RED}', end="")
            elif (nb_of_pilos != 1 and forks[i - 1] == i and
                ((i == nb_of_pilos and forks[0] == i) or forks[i] == i)):
                print(f'{const.GREEN}', end="")
            elif ((i == nb_of_pilos and forks[0] == i) or (i != nb_of_pilos and forks[i] == i)):
                print(f'{const.YELLOW}', end="")
            print(f'{i}{const.RESET}', end=" ")
            i = i + 1
        if (forks[0] == nb_of_pilos):
            print(f'[{forks[0]}]', end="")
        print()


