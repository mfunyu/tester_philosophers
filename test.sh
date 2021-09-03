#!/bin/bash

source ./tests/srcs_sh/const.sh

rm -f ./tests/logs/tester_log

single_bash_test (){
	printf "${CYAN}-------------${1}--------------${RESET}\n"
	file="${SRCS_DIR}/${1}.sh"
	$file 2> /dev/null
}

all_bash_tests (){
	for test in ${TESTS[@]}; do
		single_bash_test $test
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

print_help (){
	printf "${CYAN}Call test.sh with a cmd arg to exec single test\n${RESET}"
	for test in ${TESTS[@]}; do
		printf "$test: ./test.sh ${test:5:10}\n"
	done
}


if [ -e $1 ]; then
	all_bash_tests
	python_test
elif [ "$1" == "help" ]; then
	print_help
elif [ "$1" == "fork" ]; then
	python_test
elif [ "$1" ]; then
	single_bash_test "test_${1}"
fi