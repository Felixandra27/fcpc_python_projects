#BASIC MULTIPLICATION
#EVEN AND ODD NUMBERS TO 0 AND E
for x in range(1, 11):
    for y in range(1, 11):
       z = x * y

       if z % 2 == 0:
           print ("e", end = '\t')
       if z % 1 == 0:
           print ("o", end = '\t')
       else:
           print (x*y, end='\t')


    print()
