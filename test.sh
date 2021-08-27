#!/bin/bash

source ./tests/const.sh

for test in ${TESTS[@]}; do
	printf "${CYAN}-------------${test}--------------${RESET}\n"
	file="${DIR_PATH}${test}.sh"
	$file 2> /dev/null
done

test=fork_visualizer
file="${DIR_PATH}${test}.py"
printf "${CYAN}-------------${test}--------------${RESET}\n"
for arg in "${ARGS[@]}"; do
	$PHILO $arg | python3 $file $arg
done
