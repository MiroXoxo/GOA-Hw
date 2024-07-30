# 12)შექმენით ფუნქცია reverse_string და მიიღებს ერთ მნიშვნელობას 
# str მაგალითად შემდეგ დააბრუნეთ ეს სტრინგი შებრუნებულად
stringA="todria"
stringB="train"
def reverseString(string):
    reversedString=""
    for i in range(len(string)-1,-1,-1):
        reversedString=reversedString+string[i]
    return reversedString
print(reverseString(stringA))
print(reverseString(stringB))
print()

#13)დაწერეთ პითონის ფუნქცია, რომელიც ითვლის მართკუთხედის 
# ფართობს მისი სიგრძისა და სიგანის პარამეტრების მიხედვით.
length1=9
width1=4
def areaRectangle(length,width):
    return (length+width)*2
print(areaRectangle(length1,width1))
print()

# 14)შექმენით ფუნქცია, რომელიც ამოწმებს არის თუ არა მოცემული რიცხვი მარტივი.
def primeNumber(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
print(primeNumber(1),primeNumber(31),primeNumber(121),primeNumber(2))
