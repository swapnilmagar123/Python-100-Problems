# write the python program for the count of the number in the digit
a = int(input("Enter the number here" ))
count=0
while a>0:
    count=count+1
    a=a//10
print(count)
