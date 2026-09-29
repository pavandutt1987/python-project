# Decorators 

def logger(func):
    print("Before function executes")
    func()
    print("After function execution")
@logger
def test_logger():
    print("Testing the code")