# write the python program to print all the number which is divisiable by given number
lower =int(input("Enter the number here"))
higher =int(input("Enter the number here"))
number =int(input("Enter the number here that you want check divisiabily rule"))
for i in range(lower,higher):
    if i%number==0:
        print(i)