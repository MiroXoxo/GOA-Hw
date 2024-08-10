# 2) გამოიყენეთ ყველა კონვერტაციის ფუნქცია და 
# გააკეთეთ თითოეულზე 5-5 მაგალითი, 
# დააკვირდით და გაანალიზეთ როგორ მუშაობს თითოეული ფუნქცია
# (რა დროს მოგცათ ერორი და რა დროს არა)
numberStr="10"
numberInt=int(numberStr)
print(numberInt)

number1Str="1.57"
numbr1Float=float(number1Str)
print(numbr1Float)

number2Int=42
number2Str=str(number2Int)
print(number2Str)

myTuple=(3,2,1)
myList=list(myTuple)
print(myList)

myList1=[6,5,4]
myTuple1=tuple(myList1)
print(myTuple1)


# 3) შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 5 რციხვს,
# ხოლო ამ 5 რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია (// და %_იც),
# საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში
# + ახსენით თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს.

print("Input 5 numbers of your choice for the (a+b)/(c-d)*e//a%c equation")
a=float(input("Input a Number for a: "))
b=float(input("Input a Number for b: "))
c=float(input("Input a Number for c: "))
d=float(input("Input a Number for d: "))
e=float(input("Input a Number for e: "))
# მომხმარებელს string შეაქვს ამიტომ დამჩირდა float ფუნქციის გამოყენება
print((a+b)/(c-d)*e//a%c)
