a=[]
b = int( input(("Enter the numner of element")))
for i in range(1 ,b+1 ):
    k = int(input(("Enter the numner here")))
    a.append(k)
k=0
num=int(input("Enter hte number of counted"))
for j in a:
    if j==num:
        k=k+1
print(num,k)