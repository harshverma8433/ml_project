import logging # a module that allows you to track events that occur during the execution of the program

import os # it is a module whhich provide a way to interact with the os such as handling file paths and directories
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
logs_path = os.path.join(os.getcwd() , "logs" , LOG_FILE)

os.makedirs(logs_path , exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path , LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level = logging.INFO
)   
if __name__ == "__main__":
    logging.info("logging has started..")




    '''
 Creates a log file with a name based on the current date and time in a logs directory.
Configures the logging format and level.
Logs a message ("logging has started..") to indicate that logging has begun.

purpose - troubleshoot and debugging 
          security auditing
            Data Analysis and Reporting
            
    '''