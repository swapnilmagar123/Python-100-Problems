# write the python program to print all the number that are not divisiale by 2 and 3 in the range
lower= int(input("Enter the number in the lower range"))
higher= int(input("Enter the number in the higher range"))
for i in range(lower,higher):
    if (i%2!=0 and i%3!=0):
         print(i)
