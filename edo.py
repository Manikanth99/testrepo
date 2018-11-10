def triangle():
    n = input("Please enter a number: ")   
    if n not in [0,1]:
        for i in range(n+1):
            count = 1
            for j in range(i):
                if count == 1:
                    print (n-i)*" ",i,
                    count +=1
                else:print i,
            print
        for i in reversed(range(n)):
            count = 1
            for j in range(i):
                if count == 1:
                    print (n-i)*" ",i,
                    count +=1
                else:print i,
            print
triangle()

