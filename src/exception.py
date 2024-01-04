import sys
from src.logger import logging

def error_msg_deatils(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error aagaya meri jan vo is wali file mai [{0}] line [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_msg

class CustomException(Exception):

    def __init__(self,error_msg,error_details:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_deatils(error_msg,error_details)

    def __str__(self):
        return self.error_msg
    

if __name__ == "__main__":
    logging.info("LOgging is hauing")

    try:
        10/0
    except Exception as e:
        logging.info("gafla hogaya")
        raise CustomException(e,sys) 