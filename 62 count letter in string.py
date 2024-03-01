# write the pyhton program for printing count of a in string
string=str(input("Enter the string here"))
count=0
# print(len(string))
for i in string:
    count=count+1
    print(i)
print(count)