# write the python program for printing the string withpuut panctioation
a = '''!@#$%^&*()_+[]{}|\":'''
b = input("Enter the string")
c=""
for i in  b:
    if i not in a:
        c=c+i
print(c)