#STRING METHOD EXAMPLE
#ACTIVITY B
#SOME STRING METHODS (COOUNT, LOWERCASE, UPPERCASE, CENTER CASE)
print ("NAME : Felixandra Andal")
print ("-----------------------")
print (" ACTIVITY B ")
print ("-----------------------")
#COUNT
print ("------------------------------")
print ("COUNT")
count = 0
for letter in 'Hello World':
    if letter == 'l':
        count += 1
    elif letter == 'H':
        count += 1
    elif letter == 'o':
        count += 1
    elif letter == 'W':
        count += 1
    elif letter == 'e':
        count += 1
    elif letter == 'r':
        count += 1
    elif letter == 'd':
        count += 1
print(count,'letters found')

#LOWER CASE
print ("------------------------------")
print ("LOWER CASE")

string = "FELIXANDRA ANDAL"
print('Old String: ', string)
print("Lowercase string:", string.casefold())

#UPPER CASE
print ("------------------------------")
print ("UPPER CASE")
string = "felixandra."
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)

#CENTER CASE
print ("------------------------------")
print ("CENTER CASE")

string = "FELIXANDRA"
new_string = string.center(40)
print("Centered String: ", new_string)
