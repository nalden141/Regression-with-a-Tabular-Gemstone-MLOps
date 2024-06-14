import sys

class CustomException(Exception):

    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        print(exc_tb)
        self.lineNo=exc_tb.tb_lineno
        self.fileName=exc_tb.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return f"Error occured in python file name {self.fileName} line number {self.lineNo} error message {str(self.error_message)}"

if __name__ == "__main__" :
    try:
        a=1/0
    except Exception as e:
        print(e)
        raise CustomException(e,sys)
