#Define List
names=[]

#collect the names from users
while len(names)<10:
    acceptedName=input("Input a Name")
    names.append(acceptedName)
while len(names)>0:
    print (names.pop(0))
