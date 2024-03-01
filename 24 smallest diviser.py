# write the python program for  the smallest divisivers of the number

a = []
num =  int(input("Enter the number"))
for i in range(1, num):
    if num%i==0:
       a.append(i)
a.sort()
print(a[0])
