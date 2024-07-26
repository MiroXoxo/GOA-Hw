#გაიარეთ for ციკლი და გააკეთეთ 5 მაგალითი for ციკლებზე
#1)
print("Input A String And The Number Of Times You Want It Printed")
string=input("String: ")
y=int(input("Number Of Times To Print: "))
for i in range (0,y):
    print(string,end=" ")
print("\n")

#2)
for i in range(1,11):
    print(i,end=" ")
print("\n")

#3)
for i in range(10,0,-1):
    print(i,end=" ")
print("\n")

#4)
c=int(input("Input a Number You To Find Out it's Factorial: "))
factorial=1
for i in range(1,c+1):
    factorial=factorial*i
print(factorial)
print("\n")

#5)
import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
playerCards = []
dealerCards = []
y=2
random.shuffle(cards)
for i in range(0, 4):
    if i % 2 == 0:
        playerCards.append(cards[i])
    else:
        dealerCards.append(cards[i])
    cards.remove(cards[i])
print("Dealers Hand:\n?",dealerCards[1])
print("Your Hand:")    
for i in range(0, y):
    print(playerCards[i], end=" ")

 
 

 

