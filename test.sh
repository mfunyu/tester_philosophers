#!/bin/bash

source ./tests/const.sh

for test in ${TESTS[@]}; do
	printf "${CYAN}-------------${test}--------------${RESET}\n"
	file="${DIR_PATH}${test}.sh"
	$file 2> /dev/null
done
