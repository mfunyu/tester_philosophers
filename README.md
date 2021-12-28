# tester_philosophers

## installation
```
git clone https://github.com/mfunyu/tester_philosophers.git &&
python3 -m pip install pyparsing
```
#### directory tree
```
── philosophers
   ├── Makefile
   ├── includes
   ├── srcs
   └── tester_philosophers
```

## usage
### run all tests
```
./tester_philosophers/test.sh
```
### show help
```
./tester_philosophers/test.sh help
./test.sh arg:  [check wrong arguments]
./test.sh time: [check chronology of timestamps]
./test.sh retval: [check return values]
./test.sh advanced: [visualize fork and check for more detailded conditions]
```
### run advanced test

- add command-line arguments as the same order from `./philo`
```
./tester_philosophers/run.sh [philo_nbs] [death_time] [eat_time] [sleep_time]
```