#!/bin/bash

source ./tests/const.sh

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
