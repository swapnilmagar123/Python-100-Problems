# write the python program for printing the merge of the two list and sort it
a=[]
b=[]
aa= int(input("Enter the elements how many element are present in the list"))
for i in range(1,aa):
    k=int(input("Enter the element"))
    a.append(k)
ba= int(input("Enter the elements how many element are present in the list"))
for i in range(1, ba):
    w = int(input("Enter the element"))
    b.append(w)
new=a+b
new.sort()
print("the new list is as follow \n",new)