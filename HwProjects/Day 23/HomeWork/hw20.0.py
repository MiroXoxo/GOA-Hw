#1) შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი. 
# ფუნქციამ უნდა ჩაატაროს ყველა არითმეტიკული მოქმედება ამ ორ რიცხვს შორის.
def operations(number1,number2):
    sum=number1+number2
    sub1=number1-number2
    sub2=number2-number1
    multi=number1*number2
    div1=number1/number2
    div2=number2/number1
    return sum,sub1,sub2,multi,div1,div2
print(operations(5,2))
print()

#2) შექმენით ფუნქცია რომელსაც გადაეცემა ორი რიცხვი. 
# ამ ფუნქციამ პირველ რიცხვს მანამ უნდა დაუმატოს მეორე რიცხვი 
# სანამ ჯამი არ გახდება 100ის ტოლი ან 100ზე მეტი.
def numberPlusNumber(number1,number2):
    while number1<100:
        number1=number1+number2
    return number1
print(numberPlusNumber(68,32))
print(numberPlusNumber(73,48))
print()

#3) შექმენით ფუნქცია რომელიც ამოწმებს რიცხვი კენტია თუ ლუწი.
def evenOrOdd(number):
    if number%2==0:
        return ("The Number "+str(number)+" Is Even")
    else:
        return ("The Number "+str(number)+" Is Odd")
print(evenOrOdd(2))
print(evenOrOdd(31))
print(evenOrOdd(4))
print(evenOrOdd(0))
print()

#4) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. 
# ფუნქციამ უნდა იპოვოს ლისტში უდიდესი რიცხვი
def maxNumberList(list):
    sortedList=sorted(list)
    return sortedList[-1]
print(maxNumberList([5,28,-3,1929,553,-28]))
print()

# 5)შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. 
# ფუნქციამ უნდა იპოვოს ამ ლისტში შემავალი რიცხვების ჯამი
def sumList(list):
    sumNumbersInList=sum(list)
    return sumNumbersInList
print(sumList([5,28,-3,1929,553,-28]))
 
