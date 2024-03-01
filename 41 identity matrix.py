n = int(input("Enter the number heree"))
for i in range( 1, n ):
    for j in range( 1, n ):
      if (i==j):
          print("1" ,sep=" ",end=" ")
      else:
        print("0",sep=" ",end=" ")
    print()