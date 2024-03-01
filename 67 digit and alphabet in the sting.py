string=str(input("Enter the string here "))
count1=0
count2=0
for i in string:
    if i.isdigit():
        count1= count1+1
    if i.isalpha():
        count2= count2+1
print("digit",count1)
print("aplabet",count2)