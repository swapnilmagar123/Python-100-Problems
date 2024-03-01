a=[]
b = int( input(("Enter the numner of element")))
for i in range(1 ,b+1 ):
    k = int(input(("Enter the numner here")))
    a.append(k)
a.sort()
print(sum(a))