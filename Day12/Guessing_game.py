import random

chances = 0

a = input("wanna hard mode or soft : ").lower()

if a == "hard":
    chances = 5
    
if a == "soft":
    chances = 10
    
inval = False

if a != "hard" and a != "soft":
    inval = True
    print("Invalid Input You lose")

num = random.randint(1,101)

while chances :
    b = int(input("guess number :"))
    
    if b == num:
        print("You Guessed the correct number !! ******* You won *****")
        break
        
    elif b > num:
        print("Go lower mate!! you are better than this ")
        chances -= 1
    
    elif b < num:
        print("Go higher mate!! you are better than this ")
        chances -= 1
    
if chances == 0 and not inval :
    print("You lose ")