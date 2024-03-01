# write the pythm for printing the string in the alphabetical word in the string
a = str(input("Enter the string here "))
k=a.split()
print(k)
for i in range(len(k)):
    k[i]=k[i].lower()
# print(a)
k.sort()
print(k)