import logging

def get_logs(level, message):
    logging.basicConfig(level=level)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s: %(message)s')
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    log_method = getattr(logger, level.lower())
    log_method(message)

get_logs("DEBUG", "This is a debug message.")
get_logs("INFO", "This is an info message.")
get_logs("WARNING", "This is a warning message.")
get_logs("ERROR", "This is an error message.")
