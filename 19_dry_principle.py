import random
winning_number = random.randint(1,100)
guess = 1

game_over=False
while True:
    number=int(input("guess a number between  1 to 100 : "))
    if number ==winning_number:
        print(f"you win,and you guessed in number of {guess} times")
        break
    else:
        if number<winning_number:
            print("too low")
        else:
            print("too high")
        guess+=1
        continue
       
