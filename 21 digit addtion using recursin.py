# write the python program for the addtion of digit in the number using the recursion
l = []
def sum_digit(number) :
    if number == 0:
        return l
    digit=number%10
    l.append(digit)
    sum_digit(number//10)
number= int(input("Enter the number"))
sum_digit(number)

print(sum (l))