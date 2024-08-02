age=input("enter your age")
age=int(age)
if age==0 or age < 0:
    print("YOU CANT WATCH")
elif 0<age<=3:
    print("ticket prize : 100")
elif 3<age<=10:
    print("ticket prize : 200")  
elif 10<age<=50:
    print("ticket prize : 300")    
else:
    print("ticket prize : 10")    

# use this method to check multiple condition 