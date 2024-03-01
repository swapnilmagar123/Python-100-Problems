# write the python program for finding the root of an eqation
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c"))
r1 =(-b+((b**2-(4*a*c)))**0.5)

r2 =(-b-((b**2-(4*a*c)))**0.5)
r3 =r1/2*a
r4=r2/2*a
print(r3)
print(r4)
