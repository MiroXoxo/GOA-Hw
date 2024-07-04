# 1. მომხმარებელს შემოატანინეთ ჯერ სახელი, ხოლო შემდეგ გვარი. 
# ორივე მონაცემი შეინახეთ ცვლადებში და ბოლოს დაბეჭდეთ ერთი დიდი წინადადება, 
# რომელშიც გექნებათ სახელიც და გვარიც.
name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(f"My name is {name} and my surname is {surname}")

age=int(input("Enter your age: "))
if age < 18:
    print("You are underage")
else:
    print("You are adult")

    print("\n")

    # 2. შექმენით ცვლადი, სადაც შეინახავთ თქვენთვის სასურველ რიცხვს. 
    # შემდეგ შექმენით მეორე ცვლადი, სადაც მომხმარებელს შემოატანინებთ რიცხვს. 
    # თქვენი დავალებაა, რომ დაბეჭდოთ ამ ორი რიცხვის ჯამი.
myNumber=5
userNumber=int(input("Input any number to find out the sum of it and my secret number "))
sum=myNumber+userNumber
print("The sum of",myNumber,"and",userNumber,"is",sum)

print("")

# 3. შექმენით სამი ცვლადი, თითოეულში შეინახეთ რიცხვი. თქვენი დავალებაა, 
# რომ ამ სამი რიცხვის ჯამი გაყოთ მათ რაოდენობაზე და დაბეჭდოთ ეს შედეგი.
x=7
y=4
z=10
sum=x+y+z
variablesQuantity = len([x, y, z])
print(sum//variablesQuantity)

print("")

# 4. პირველ რიგში, მომხმარებელს შემოატანინეთ სთრინგი და ის გაამრავლეთ ხუთზე.
# შემდეგ შემოატანინეთ რიცხვი და ისიც გაამრავლეთ ხუთზე. ორივე შედეგი დაბეჭდეთ და
# კომენტარების გამოყენებით აღწერეთ თითოეული.
userStr=input("Input any string to be multiplied by 5: ")
userInt=int(input("Input any Integer to be multiplied by 5: "))
print(userStr*5)
print(userInt*5)

















 
