# write the pyhton for printing counting the vowel in the string
string= str(input("Enter the string here"))
count=0
for chr in string:
 if chr =="a":
     count=count+1
 if chr =="e":
     count=count+1
 if chr =="i":
     count=count+1
 if chr == "o":
     count=count+1
 if chr =="u":
     count=count+1
print(count)