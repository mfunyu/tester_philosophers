#!/bin/bash

source ./tests/const.sh
. ./tests/print_result.sh

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
			print_result $?
		fi
	done
	printf "\n"

}

rm $LOG_FILE
clonology_test
