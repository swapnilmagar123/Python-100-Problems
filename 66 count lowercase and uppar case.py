string=str(input("Enter the string here "))
count1=0
count2=0
for i in string:
    if i.islower():
        count1= count1+1
    if i.isupper():
        count2= count2+1
print("lowwercase",count1)
print("uppercase",count2)