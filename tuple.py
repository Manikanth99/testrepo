li=[-2,-3,-4,-5,-6,-7,-8,2,3,4,5,6,7,8,10,12,14,15,16,17,18,19,20]
l2=[]
for i in li:
	for j in li[i+1:]:
		if i+j==12:
                    if (j,i) not in l2:
                        l2.append((i,j))
print l2 
