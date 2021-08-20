#!/bin/bash

DIR_PATH=./tests/

TESTS=(
"test_arg"
"test_time"
)
# define
THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[33m"
RESET="\033[m"
PROMPT="${CYAN}$>${RESET}"

for test in ${TESTS[@]}; do
	printf "${CYAN}-------------${test}--------------${RESET}\n"
	file="${DIR_PATH}${test}.sh"
	$file
done
