import logging, datetime, config

def get_logger(logger_name="chat_log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    # create file handler which logs even debug messages
    now = datetime.datetime.now()
    log_dir = config.LOGGER_DIR
    fh = logging.FileHandler("{}{}.log.{}{}".format(log_dir, logger_name, now.year, now.strftime("%m%d")))
    fh.setLevel(logging.INFO)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger