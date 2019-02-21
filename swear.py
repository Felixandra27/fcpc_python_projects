#SWEAR
print ("NAME : Felixandra Andal")
print ("-----------------------")
print (" ACTIVITY B ")
print ("-----------------------")

stringinp = "tanga, kang bobo ka!"

listd = stringinp.split()

wordlist = ["tanga", "bobo"]

hasdetected = False

for word in listd:
    for swear in wordlist:
        # if swear == word:
        if word.find(swear) >-1:
            print("-" *len(swear),end = "_")
            hasdetected = True
            break
        else:
            hasdetected = False
    if not hasdetected:
        print(word, end =" ")
