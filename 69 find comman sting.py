# write the pyhton program for checking given common characher in the string

string1=str(input("Enter the string here"))
string2=str(input("Enter the string here"))
a=list(set(string1)and set(string2))

print(a)