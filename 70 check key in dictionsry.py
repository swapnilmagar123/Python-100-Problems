# Write the python program for printing check key in the dictionary
d ={"S":1,"D":1,"B":1}
key = input("enter the key here")
if key in d.keys():
    print("key is present and the value is ",d[key])
else:
    print("key is not present")
