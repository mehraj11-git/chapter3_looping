winning = 50
guess = 1
number = input("guess the number")
number =int(number)
gameover = False
while not gameover:
    if number == winning:
     print(f"you win,and you guessed this number in {guess} times")
     gameover=True
    else:
       if number < winning:
          print("too low")
          guess +=1
          number=int(input("guess again"))
       else:
          print("too high")
          guess += 1
          number=int(input("guess again"))
# number guessing game
# make a variable,like winning_number and assign any number to it: 
# ask user to guess the number
# if user guessed correctly then print "YOU WIN"!
# if user guessed higher or lower than the actual numbere print "too high" or "too low"
