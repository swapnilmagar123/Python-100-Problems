# write the pyhton program for the printing lcm of the two number
a = int(input("Enter the first number "))
b = int(input("Enter the  second number"))
if a>b:
    smaller=b
if a<b:
    smaller=a
for i in range(2,smaller):
    if a%i==0 and b%i==0:
        print(i)
    # else:
    #   print(" ")