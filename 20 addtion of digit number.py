# write the python program for the addtion of digit in the number
number= int(input("Enter the number here"))
sum=0
while(number>0):
    digit=number %  10
    sum= sum + digit
    number=number//10
print(sum)