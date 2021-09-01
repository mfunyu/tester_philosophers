#!/bin/bash

source ./tests/srcs_sh/const.sh

rm -f ./tests/logs/tester_log

bash_test (){
	for test in ${TESTS[@]}; do
		printf "${CYAN}-------------${test}--------------${RESET}\n"
		file="${SRCS_DIR}/${test}.sh"
		$file 2> /dev/null
	done
}

python_test (){
	test=fork_visualizer
	file="${DIR_PATH}${test}.py"
	printf "${CYAN}-------------${test}--------------${RESET}\n"
	for arg in "${ARGS[@]}"; do
		printf "${PROMPT} ${PHILO} ${arg}${RESET}\n"
		$PHILO $arg | python3 $file $arg
	done
}

if [ -e $1 ]; then
	bash_test
	python_test
elif [ "$1" == "fork" ]; then
	python_test
fi