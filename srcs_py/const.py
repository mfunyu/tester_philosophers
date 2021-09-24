FILE = "./tests/logs/log"
LOG_FILE='./tests/logs/tester_log'


THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
GRAY="\033[38;5;240m"
RESET="\033[m"

fork="has taken a fork"
eat="is eating"
sleep="is sleeping"
think="is thinking"
died="died"

ERR_FLAG_PRIFORMAT = 0b1
ERR_FLAG_FORK = 0b10
ERR_FLAG_DEATH = 0b100
ERR_FLAG_EOS = 0b1000
FLAG_LST = [ERR_FLAG_PRIFORMAT, ERR_FLAG_FORK, ERR_FLAG_DEATH, ERR_FLAG_EOS]
FLAG_INFO = {
ERR_FLAG_PRIFORMAT: "log format	  ",
ERR_FLAG_FORK: "no stolen fork	  ",
ERR_FLAG_DEATH: "death time	  ",
ERR_FLAG_EOS: "end of simulation ",
}
ERROR_FLAGS = 0
