# write the python program for the checking the prime number
number= int(input("Enter the number"))
if number==1:
    print("1 is not a prime and composite number")
if number>1:
 for i in range(2, number):
    if number%i==0:
      print("This number  not is  prime")
      break
 else:
        print("this is the  prime number")