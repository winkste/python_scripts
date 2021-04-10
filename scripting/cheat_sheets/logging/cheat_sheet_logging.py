#this cheat sheet explains basic logging funcions
#https://docs.python.org/3/howto/logging.html
#https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

#import the logging module
import logging
import logging.config
import sys
import os


#----------------------------------------------------------------------------------------
# simple logging mechanism
def display_all_log_levels():
    logging.info('This is an info message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')


# NOTE: the basicConfig function can only be called once, ensure
#       settings are correct for the complete project

# changing the message level 
logging.basicConfig(level=logging.DEBUG)
display_all_log_levels()

# configuring to log to a file (appending)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
display_all_log_levels()

# configuring to log to a file (overwriting)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
display_all_log_levels()

#----------------------------------------------------------------------------------------
# more detailed configuration using a config file for setup
logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')
# creating a logger with the current file name as handler/key
logger2 = logging.getLogger(os.path.basename(__file__).split(".")[0])


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger2.debug('debug message')
logger2.critical('critical message')


#result looks like:
#2021-03-26 05:56:45,793 - simpleExample - DEBUG - debug message
#2021-03-26 05:56:45,793 - simpleExample - INFO - info message
#2021-03-26 05:56:45,794 - simpleExample - WARNING - warn message
#2021-03-26 05:56:45,794 - simpleExample - ERROR - error message
#2021-03-26 05:56:45,794 - simpleExample - CRITICAL - critical message