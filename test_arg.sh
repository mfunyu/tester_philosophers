#!/bin/bash

PHILO=./philo

# define
THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[33m"
RESET="\033[m"
PROMPT="${CYAN}$>${RESET}"

ERR_CHECK=(
""
"1"
"1 1 1"
"1 1 1 1 1 1"
"aaa 1 2 3"
"1 aaa 2 3 4"
"2147483649"
"aaa bbb ccc ddd eee"
)

ARGS=(
"3 200 400 800"
)

normal_test (){
	for arg in "${ARGS[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}\n"
		$PHILO $arg
	done
}

error_test (){
	for arg in "${ERR_CHECK[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}\n"
		$PHILO $arg
	done
}


error_test
normal_test