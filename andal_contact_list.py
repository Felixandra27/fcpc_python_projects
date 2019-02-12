#DICTIONARY
print ("NAME : Felixandra Andal")
print ("-----------------------")
print (" ACTIVITY B ")
print ("-----------------------")

dict={ }
dict["FIRST NAME"]= input("Enter first name:")
dict["LAST NAME"]= input("Enter last name:")
dict["AGE"]= int(input("Enter age:"))
dict["CONTACT NUMBER"]= int(input("Enter Contact Number:"))
print (dict)
for key in dict:
    print(dict[key])
dict1={}
dict2=[]
while True:
    dict1["First NAME"]=str(input("Enter First Name: "))
    if dict1["First NAME"]== "XXX":
        break
    else:
        dict1["LAST NAME"]=str(input("Enter Last Name: "))
        dict1["AGE"]=int(input("Enter Age: "))
        dict1["CONTACT NUMBER"]= int(input("Enter Contact Number:"))
        A.append(dict1)
        print(dict1)
        for dict2 in dict1:
            print(dict1[dict2])