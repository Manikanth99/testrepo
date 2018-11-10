def reverse(a):
    c = a[::-1]
    d = ''
    for i in range(len(a)):
        if a[i] == ":" or c[i]==":":
            d = d+a[i]  
        else:d=d+c[i]
    return d
print reverse("asdas:asda:ad")



