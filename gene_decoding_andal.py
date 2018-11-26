print("THIS IS EXAMPLE OF DECODING !!!")
name_1 = input("Please Enter your Name:") #ABC-DEF-GHI-JKL-MNO-PQR-STU-VWX-ZZZ
name_2 = ""

for x in range(len(name_1)) :
    char = name_1[x]
    if char == "A":
        name_2 += "B"
    elif char == "B":
        name_2 += "C"
    elif char == "C":
        name_2 += "D"
    elif char == "D":
        name_2 += "E"
    elif char == "E":
        name_2 += "F"
    elif char == "F":
        name_2 += "G"
    elif char == "G":
        name_2 += "H"
    elif char == "H":
        name_2 += "I"
    elif char == "I":
        name_2 += "J"
    elif char == "J":
        name_2 += "K"
    elif char == "K":
        name_2 += "L"
    elif char == "L":
        name_2 += "M"
    elif char == "M":
        name_2 += "N"
    elif char == "N":
        name_2 += "O"
    elif char == "O":
        name_2 += "P"
    elif char == "P":
        name_2 += "Q"
    elif char == "Q":
        name_2 += "R"
    elif char == "R":
        name_2 += "S"
    elif char == "S":
        name_2 += "T"
    elif char == "T":
        name_2 += "U"
    elif char == "U":
        name_2 += "V"
    elif char == "V":
        name_2 += "W"
    elif char == "W":
        name_2 += "X"
    elif char == "X":
        name_2 += "Y"
    elif char == "Y":
        name_2 += "Z"
    elif char == "Z":
        name_2 += "A"
    else:
        name_2 += char

print(name_2)
