# write the python program for printing count in the string as the lower alphabet
string=str(input("Enter the string here"))
count=0
for i in string:
    if (i.islower()):
        count=count+1
print(count)
