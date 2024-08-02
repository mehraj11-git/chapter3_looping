name =input("enter your name : ")
i = 0
tem_var= ""
while i < len(name):
    if name[i] not in tem_var:
       tem_var+=name[i]
       print(f"{name[i]} : {name.count(name[i])}")
    i +=1


# ask user name
# ex: mehraj uddin
# print count of each words
# output:
# m:1
# e:1
# h:1
# r:1
# a :1
#  j :1       
# if we donot value of i then it will make it infinite