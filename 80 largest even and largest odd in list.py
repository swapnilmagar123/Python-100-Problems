# write the pyhton program for printing the largest even and the largest odd number in the list
a = int(input("Enter the number here"))
c=[]
for i in range(1 ,a+1):
    b= int(input("Enter the element here"))
    c.append(b)
d=[]
e=[]
for i in c:
    if i%2==0:
        d.append(i)
    else:
        e.append(i)
d.sort()
e.sort()
count1=0
count2=0
for m in d:
    count1=count1+1
for n in e:
    count2=count2+1
print(d[count1-1])
print(e[count2-1])
