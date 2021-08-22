#!/bin/bash

DIR_PATH=./tests/

TESTS=(
"test_arg"
"test_time"
)

PHILO=./philo

LOG_FILE=./tests/log
TMP_FILE=./tests/tmp

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
"5 800 400 100"
"15 200 400 800"
)

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