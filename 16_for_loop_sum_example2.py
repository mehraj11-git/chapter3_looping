name = input("enter your name : ")
temp = ""
for string in range(0,len(name)):
    if name[string] not in temp :
        print(f"{name[string]} : {name.count(name[string])}")
    temp+=name[string]