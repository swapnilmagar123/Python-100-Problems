# write the python program for the checking the prime number in the range
lower=int(input("Enter the lower range"))
higher=int(input("Enter the higher range"))
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
                print(num)
