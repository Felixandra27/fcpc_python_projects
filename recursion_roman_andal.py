# #RECUSION
# def abc():
#     print("Hi")
#     abc()
# #abc() # tail recursion
# #STUCK OVER FLOW
print ("FELIXANDRA F. ANDAL")
def toRomanNum(x):
    if x <= 200:
        if x == 200:
            print("CC", end="")
        elif x == 100:
            print("C", end="")
        elif x < 200 and x > 150:
            print("C", end="")
            a = x - 100
            toRomanNum(a)
        elif x == 99:
            print("IC", end="")
        elif x <= 98 and x >= 50:
            print("L", end="")
            b = x - 50
            toRomanNum(b)
        elif x == 49:
            print("IL", end="")
        elif x <= 48 and x >= 40:
            print("XL", end="")
            c = x - 40
            toRomanNum(c)
        elif x <= 39 and x >= 10:
            print("X", end="")
            d = x - 10
            toRomanNum(d)
        elif x <= 9 and x >= 5:
            print("V", end="")
            e = x - 5
            toRomanNum(e)
        elif x < 5 and x > 0:
            print("I", end="")
            f = x - 1
            toRomanNum(f)
        else:
            print()

toRomanNum(100)
#"romannumber"
