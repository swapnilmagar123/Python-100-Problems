# write the python program for checking the leap year
a = int(input("Enter the age"))
if a%100 !=0 and a % 4==0 or  a % 400==0:
    print("this is a leap year")
else:
    print("this is not leap year")
