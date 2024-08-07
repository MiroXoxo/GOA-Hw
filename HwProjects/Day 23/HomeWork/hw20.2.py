# 9)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი. 
# ამ ფუნქციის მეშვეობით უნდა დაითვალოთ თანხმოვნების რაოდენობა ამ სტრინგში.
def consonantCount(string):
    consonants=0
    consonantsMinusY=["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    if string[0].lower()=="y":
        consonants+=1
    for i in range(len(string)):
        if string[i]==" " and string[i+1].lower()=="y":
            consonants+=1
        elif string[i].lower() in consonantsMinusY:
            consonants+=1
    return consonants
print(consonantCount("That Is A Yellow Volleyball"))
print()

#10)შექმენით ფუნქცია რომელსაც გადაეცემა ინტეჯერი და თუ ლუწია 
# აბრუნებს True-ს ხოლო თუ კი კენტია აბრუნებს False
def isEven(integer):
    return integer%2==0
print(isEven(5))
print(isEven(2))
print(isEven(0))
print()

#11)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. 
# თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. 
# აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.
list1=[22,-38,92,26,-2,0,17]
def sumOfEvenIndexes(list):
    sumEvenIndex=0
    for i in range (len(list)):
        if i%2==0:
            sumEvenIndex=sumEvenIndex+list[i]
    return sumEvenIndex
print(sumOfEvenIndexes(list1))
print()

#12)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, 
# რომ დააბრუნოთ ლუწია თუ კენტი ის.
def oddOrEven(integer):
    if integer%2==0:
        return ("Even")
    else:
        return ("Odd")
print(oddOrEven(5),oddOrEven(0),oddOrEven(12))
print()

