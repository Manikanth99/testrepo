import string
from random import shuffle
def Generate_pswd():
    chars = list(string.ascii_letters+string.digits)
    #print chars
    shuffle(chars)
    return "".join(chars[:8])

class A:
    def __init__(self):
        pass
    def func(self):
        print "IN Class A"

class B(A):
    def __init__(self):
        pass
    def func(self):
        print "In Class B...Class A's function will be called now"
        A().func()

        
