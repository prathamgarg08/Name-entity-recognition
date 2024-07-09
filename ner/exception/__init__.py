import os 

def error_message_detail(error,error_detail):
    _, _, exc_tb=error_detail.exc_info()

    file_name=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message= 'error occured in python script [{0}] line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno, str(error)
    )

    return error_message

class NerException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message) # super is used to call Exception
        self.error_message=error_message_detail(
        error_message,error_detail=error_detail
    )

    def __str__(self):
        return self.error_message