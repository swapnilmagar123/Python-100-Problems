# write the  pyhton program gravitational for two mass and raduis
m1=int(input("Enter the first mass"))
m2=int(input("Enter the second mass"))
r=int(input("Enter the radius "))
G=6.67*(10**-11)
g= (m1*m2*G)/r**2
print(round(g,2))