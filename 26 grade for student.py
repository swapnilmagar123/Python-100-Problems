# write the python program for the grading system of the student
maths = int(input("Enter the marks of maths"))
marathi = int(input("Enter the marks of marathi"))
english = int(input("Enter the marks of english"))
biology = int(input("Enter the marks of biology"))
chemistry = int(input("Enter the marks of chemistry"))
avg1 =((maths+marathi+english+biology+chemistry))
avg = (avg1/500)*100
if avg>90:
    print("grade A",avg )
elif avg>80:
    print("grade B",avg)
elif avg>70:
    print("grade C",avg)
elif avg>50:
    print("grade d",avg)
else:
    print("Fail",avg)