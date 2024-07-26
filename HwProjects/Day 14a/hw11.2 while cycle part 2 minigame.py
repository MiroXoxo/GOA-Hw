#5)
import random
secretNumber=random.randrange(1,15)
x=0
y=0
print("Guess The Secret Number Between 0 and 15\nYou Have 5 Tries\nGood Luck!")
while x!=secretNumber and y<5:
    x=int(input("Your Number: "))
    if x<secretNumber and y!=4:
        print("Higher")
    elif x>secretNumber and y!=4:
        print("Lower")
    elif x==secretNumber:
        print("Correct The Secret Number Is",secretNumber)
    y+=1
    if y==5:
        print("You Used Up All Your Tries Try Again")