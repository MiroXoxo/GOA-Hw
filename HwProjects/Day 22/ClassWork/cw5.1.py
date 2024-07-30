# 7)შექმენით ფუნქცია  print_even_numbers რომელიც მიიღებს 
# ერთ პარამეტრს n შემდეგ გამოიტანს 2 დან ამ რიცხვამდე 
# ყველა ლუწ რიცხვს გამოიყენეთ for loop
n=17
def printEvenNumbers(endNumber):
    for i in range(2,n):
        if i%2==0:
            print(i,end=" ") 
printEvenNumbers(n)
print("\n")

#8)შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) 
# ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ 
# num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დაბეჭდეთ
a=9
b=12
def sum(number1,number2):
    print(number1+number2)
sum(a,b) 
print()

# 9)შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) 
# ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ 
# num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დააბრუნოთ
a=9
b=52
def sum(number1,number2):
    return number1+number2
print(sum(a,b))
print()

# 10)შექმენით ფუნქცია რომელიც დაბე#ჭდავს ორი სტრინგის გაერთიანებას 
# მაგალითად str1  და str2 და დაბეჭდეთ 
# მათი შეერთება ფუნქციას დაარქვით joined_string
stringA="Break"
stringB="Fast"
def joinedString(string1,string2):
    print(stringA+stringB)
joinedString(stringA,stringB)
print()

# 11)შექმენით ფუნქცია find_maximum რომელსაც გადაასცემთ ორ მნიშვნელობას 
# მაგალიტად num1 და num2 შემდეგ დააბრუნეთ აქედან რომელიც უფრო მეტია
a=374
b=293
def findMaximum(number1,number2):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return f"{number1}={number2}"
print(findMaximum(a,b))
 

