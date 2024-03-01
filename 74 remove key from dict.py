# write the pyhotn program for remove key form dict
d ={"a":10,"ga":10,"bg":8,"b":5,}
print("initial dict",d)
key = input("Enter the key here")
if key in d :
    del d[key]
else:
    print("key not foung")
    exit(0)
print("upadated dict")
print(d)