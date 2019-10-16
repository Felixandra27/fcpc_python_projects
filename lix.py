print("Felixandra F. Andal")
print("-------------------")
while True:
    matrixResult = []
    print("MATRIX A")
    A1 = int(input("Input ROW/S: "))
    B1 = int(input("Input COLUMN/S: "))
    matrixA = []
    for x in range(0, B1):
        matrixA.append([]) # .APPEND IS TO SHOW MATRIX RESULT
        for y in range(0, A1):
            matrixA[x].append(0)
            matrixA[x][y] = int(input("Enter Numbers in Row/s and Column/s: "))
    print(matrixA)
    print("-----------------------------------------")
    print("MATRIX B")
    print("-----------------------------------------")
    A2 = int(input("Input ROW/S: "))
    B2 = int(input("Input COLUMN/S: "))
    print(A2, B2)
    matrixB = []
    for x in range(0, B2):
        matrixB.append([])
        for y in range(0, A2):
            matrixB[x].append(0)
            matrixB[x][y] = int(input("Enter Element: "))
    print("Matrix 1 ")
    print(matrixA)
    print("Matrix 2 ")
    print(matrixB)
    print("------------------------------------------")
    print("CHOOSE SPECIFIC COMPUTATION")
    print("[1.]-ADDITION FOR THE MATRIX")
    print("[2.]-MULTIPLICATION FOR THE MATRIX")
    resultInput = int(input("Selected Number is : "))
    if resultInput == 1:
        for x in range(len(matrixA)):
            for y in range(len(matrixA[0])):
                matrix = matrixA[x][y] + matrixB[x][y]
                matrixResult.append(matrix)
        print("Added Matrices : ", matrixResult)
        break
    if resultInput == 2:
        if B1 == A2:
            multResult = [[sum(x * y for x, y in zip(matrixA_r, matrixB_c)) for matrixB_c in zip(*matrixB)] for
                          matrixA_r in matrixA]
        print("Multiplied Matrices : ", multResult) # MULTIPLICATION RESULT
        break
    else:
        print("Invalid Elements") # INVALID MATRICES
        break
