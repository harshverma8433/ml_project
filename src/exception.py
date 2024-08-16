import sys 
# provide access to system-specific parameters and functions . it is used to extrct the error details such as file name and line no where exception occur

import logging 
# it is python builtin module . it is used to log the messages and errors in the application when exception caught

from src.logger import logging

def error_message_detail(error , error_details:sys):
    _,_,exc_tb = error_details.exc_info() # return a tuple containing the type , value and traceback of the recent exception
    file_name = exc_tb.tb_frame.f_code.co_filename # get the file name where exception occured
    error_message = "Error Occured in Python Scripts name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide By Zero")
        raise CustomException(e , sys)