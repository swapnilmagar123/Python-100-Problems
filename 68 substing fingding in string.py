# write the pyhton program for checking given substing in the string

string=str(input("Enter the string here"))
sub_string=str(input("Enter the word here"))
if( string.find(sub_string)==True):
    print("substring is  not present")
else:
    print("substring is  present")