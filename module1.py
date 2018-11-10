class A:
    def F1(self,a,b):
        print a+b
        print A().F2()
    def F2(self):
        print A().F3()
        return "F2"
    def F3(self):
        return "F3"

class B(A):
    def F1(self,a,b):
        print F3()
        print "Class B Function A"

if __name__ == "__main__":
    A().F1(1,2)
    B().F1(1,1)
    b = B()
    

    
