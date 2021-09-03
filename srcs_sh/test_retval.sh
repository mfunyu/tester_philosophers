#!/bin/bash

# number of times for the execution loop
NTIME=100

# set up
SRCS_DIR=$(dirname $0)
source ${SRCS_DIR}/const.sh
error=0

# funcs
exec_loop () {
	for i in `seq ${NTIME}` ; do
		${PHILO} 20 200 400 800 > /dev/null
		result=$?
		if [ $result == 0 ]; then
			printf "${GREEN}.${RESET}"
		elif [ $result == 139 ]; then
			printf "${RED}C${RESET}"
			error=$((error + 1))
		elif [ $result == 134 ]; then
			printf "${RED}A${RESET}"
			error=$((error + 1))
		else
			printf "${RED}${result}${RESET}"
			error=$((error + 1))
		fi
	done
}

print_sum () {
	if [ $error == 0 ]; then
		printf "\n${GREEN}OK :) ${RESET} no error found!\n"
	else
		printf "\n${RED}KO :(${RESET} ${error} errors found\n"
	fi
}

main () {
	printf "n = ${NTIME}\n"
	exec_loop
	print_sum
}

main