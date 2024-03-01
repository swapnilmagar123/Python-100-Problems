# write the pyhton program for printing count of a in string
string=str(input("Enter the string here"))
count=0
# print(len(string))
for i in string:
    if i=="a":
      count=count+1

print( "coint of a is ",count)