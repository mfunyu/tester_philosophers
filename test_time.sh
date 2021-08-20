#!/bin/bash

PHILO=./philo

LOG_FILE=./tests/log

# define
THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
RESET="\033[m"
PROMPT="${CYAN}$>${RESET}"

ARGS=(
"3 200 400 800"
"3 600 400 100"
"3 800 400 100"
)

check_okko (){
	if [ $? == $1 ]; then
		printf "${GREEN}KO :) ${RESET}\n"
	elif [ $? == 139 ]; then
		printf "${RED}KO :( [Crash!] ${RESET}\n"
	else
		printf "${RED}KO :(${RESET}\n"
	fi
}

clonology_test (){
	printf "${CYAN}[${FUNCNAME[0]}]${RESET}\n"
	for arg in "${ARGS[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}\n"
		echo "${PHILO} ${arg}\n" >> $LOG_FILE
		$PHILO $arg >> $LOG_FILE
		if [ $? == 139 ]; then
			printf "${RED}KO :( [Crash!] ${RESET}\n"
		else
			log=cat $LOG_FILE | awk '{print$1}'
			diff <( $log | sort -n) <($log)
			check_okko 0
		fi
	done
	printf "\n"

}

rm $LOG_FILE
clonology_test
