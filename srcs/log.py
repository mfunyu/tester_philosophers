import logging
from srcs import const

logger = logging.getLogger("logger")    #logger名loggerを取得
logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで
#handlerを作成
handler = logging.FileHandler(filename=const.LOG_FILE, mode='w')
handler.setFormatter(logging.Formatter("%(filename)8s: %(message)s"))
logger.addHandler(handler)

def set_error_print_log(error, **kwargs):
    const.ERROR_FLAGS |= error
    if error == const.ERR_FLAG_FORK:
        logger.debug(f"the fork philosopher {kwargs['philo_nb']} grabbed was not yet released")
    elif error == const.ERR_FLAG_DEATH:
        logger.debug(f"the philosopher {kwargs['philo_nb']} died at wrong time.\n\
the philosopher {kwargs['philo_nb']} was supposed to die at {kwargs['time_exp']}, \
but died at {kwargs['time_act']}; {kwargs['time_exp'] - kwargs['time_act']}ms late")
    elif error == const.ERR_FLAG_EOS:
        logger.debug(f"operation after death")

