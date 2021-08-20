#!/bin/bash

PHILO=./philo

# define
THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[m"
PROMPT="${CYAN}$>${RESET}"

ERR_CHECK=(
""
"1"
"-1234"
"1 1 1"
"1 1 1 1 1 1"
"aaa 1 2 3"
"1 aaa 2 3 4"
"2147483648"
"-2147483649"
"1000000000000000000"
"0.001 1.25 123 567 8"
"aaa bbb ccc ddd eee"
"42424242424242Tokyo"
)

ARGS=(
"3 200 400 800"
)

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