name,age=input("enter your name and age").split()
age=int(age)
if age>=10 and (name[0]=="a" or name[0]=="A"):
    print("YOU CAN WATCH COCO")
else:
    print("sorry,you can't watch the coco")

# ask the user name and age 
# if user name start with ("a" or "A")nand age is above 10 then print "YOU CAN WATCH COCO MOVIE"
# ELSE print 'sorry you can play'