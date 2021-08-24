#!/bin/bash

function print_result (){
	if [ $? == $1 ]; then
		printf "${GREEN}OK :) ${RESET}\n"
	elif [ $? == 139 ]; then
		printf "${RED}KO :( [Crash!] ${RESET}\n"
	elif [ $? == 134 ]; then
		printf "${RED}KO :( [Abort!] ${RESET}\n"
	else
		echo $?
		printf "${RED}KO :(${RESET}\n"
	fi
}