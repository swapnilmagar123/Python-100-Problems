# write the pyhton program for addtion of the prime numger in the range
lower = int(input("Enter the lower number here"))
higher = int(input("Enter the higher number here"))
a=[]

for num in range(lower, higher+1):
    if num>1:
        for i in range(2,num ):
           if num%i==0:
               break
        else:
             print(num)
             a.append(num)
a.sort()
print(a)
print("the addition of the prime number",sum(a))



# # write the python program for the checking the prime number in the range
# lower=int(input("Enter the lower range"))
# higher=int(input("Enter the higher range"))
# for num in range(lower,higher+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#                 print(num)