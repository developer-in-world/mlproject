import sys
import logging


def error_message_detail(error, error_detail:sys):
    '''
    Docstring for error_message_detail
    
    :param error: error name
    :param error_detail: It helps us to understand what error error has occured in what line by using exc_info()
    :type error_detail: sys
    '''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message # prints the error message