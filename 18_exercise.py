winning_number =8
user = input("guess the number between 1 to 20 : ")
user = int(user)
if winning_number == user:
    print("YOU WIN !!!")
else:
    if winning_number >= user :
        print("too low") 
    if winning_number <= user :
        print("too high")   

