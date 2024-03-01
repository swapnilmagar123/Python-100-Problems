# write the pyhon program for printing the largest element in the list
a=[]
b = int( input(("Enter the numner of element")))
for i in range(1 ,b+1 ):
    k = int(input(("Enter the numner here")))
    a.append(k)
a.sort()
print("this is the largest number in the given number",a[-1])
