#!/bin/bash

source ./tests/const.sh

check_okko (){
	if [ $? == $1 ]; then
		printf "${GREEN}	KO :) ${RESET}\n"
	elif [ $? == 139 ]; then
		printf "${RED}	KO :( [Crash!] ${RESET}\n"
	else
		printf "${RED}	KO :(${RESET}\n"
	fi
}

normal_test (){
	printf "${CYAN}[${FUNCNAME[0]}]${RESET}\n"
	for arg in "${ARGS[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}\n"
		$PHILO $arg > /dev/null
		check_okko 0
	done
	printf "\n"
}


ERR_MSG="Error: Invalid argument"

arg_error_test (){
	printf "${CYAN}[${FUNCNAME[0]}]${RESET}\n"
	for arg in "${ERR_CHECK[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}"
		if [ $1 ]; then
			diff <(echo $ERR_MSG) <(${PHILO} ${arg} 2>&1)
			check_okko 0 #no diff
		else
			printf "\n"
			$PHILO $arg
		fi
	done
	printf "\n"
}


arg_error_test mine
normal_test