# write the pyhton program for removing the duoplicate elements
a = []
num= int(input("Emter the number here"))
for i in range(1,num+1):
    k= int(input("Enter the number here"))
    a.append(k)
king=set()
unique=[]
for i in (a):
    if i not in king:
        unique.append(i)
        king.add(i)
print("this is the non duplicate item",unique)