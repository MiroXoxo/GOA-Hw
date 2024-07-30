#1) შექმენით ფუნქცია რომელსაც დაარქმევთ Calculate_average სადაც 
# იქნება ერთი სია შექმნილი სახელად numbers თქვენი დავალება არის 
# გამოთვალოთ ამ რიცხვების საშუალო არითმეტიკული გამოიყენეთ  
# sum და len ფუნქციები
numbers=[4,8,-9,16,1]
def calculateAverage(listNumbers):
    avrg=str(sum(listNumbers)/len(listNumbers))
    while avrg[-1]=="0" or avrg[-1]==".":
        avrg=avrg[:-1]
    return avrg
print(calculateAverage(numbers))
print()

#2)შექმენით ფუნქცია manual_sum ჩვენი ფუნქცია მიიღებს ერთ მნიშვნელობას სიას. 
# თქვენი დავალება არის გაიგოთ ამ სიის რიცხვთა ჯამი for ციკლის მეშვეობით
numbers=[4,8,-9,16,1,53,-23]
def manualSum(numbersList):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
print(manualSum(numbers))
print()

#3) შექმენით  მისალმების ფუნქცია სახელად greet რომელიც 
# მიესალმება მომხმარებელს და 
# default მნიშვნელობად იქნება hello guest
def greet(adminOrGuest):
    if adminOrGuest=="Miro":
        print("Hello Admin")
    else:
        print("Hello Guest")
greet("Jojo")
greet("Miro") 
print()

# 4)შექმენით ფუნქცია რომელსაც გადაეცემა ორი მნიშვნელობა 
# firstnum და secondnum და თქვენი დავალებაა იპოვოთ 
# ამ რიცხვებს შორის ყველა რიცხვის ჯამი
def sum(number1,number2):
   return number1+number2
print(sum(55,22))
print()

#5) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. 
# თქვენი დავალებაა ამ ლისტიდან ამოიღიოთ ყველა ციფრი და 
# დაახარისხოთ ისინი კენტებად და ლუწებად
list=[4,17,5,81,90,22,54,3]
def sortEvenOrOdd(listToSort):
    listEven=[]
    listOdd=[]
    for i in range(0,len(listToSort)):
        if listToSort[i]%2==0:
            listEven.append(listToSort[i])
        else:
            listOdd.append(listToSort[i])
    return listEven,listOdd
print(sortEvenOrOdd(list))
print()

#6)შექმენით ფუნქცია print_numbers რომელიც მიიღებს n 
# მნიშვნელობას და გამოიტანს 1 დან ამ n რიცხვამდე ყველა 
# რიცხვს for loop ის გამოყენებით
n=12
def printNumbers(endNumber):
    for i in range(1,n):
        print(i,end=" ")
printNumbers(n)
print("\n")




