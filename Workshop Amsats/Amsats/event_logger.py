# amsat_utils/event_logger.py

import logging
import os

def configure_log(log_file='logfile.log', console_level=logging.INFO,
                  file_level=logging.DEBUG, log_level=logging.DEBUG):
    """
    A hopefully functional logger for the AmSat notebook.
    Only needs to be called once.
    """

    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # make sure re-running a cell doesn't create new handlers
    if logger.handlers:
        for handler in list(logger.handlers):
            logger.removeHandler(handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_level)

    # make a custom formatter here to keep track of things
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("Logging configuration initialized.")

try:
    configure_log()
except Exception as e:
    print(f"Failed to setup logging: {e}")
