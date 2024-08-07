#13)შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი 
# (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს).
def isPrimeNumber(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
print(isPrimeNumber(71),isPrimeNumber(31),isPrimeNumber(121),isPrimeNumber(2),isPrimeNumber(1))
print()

#14)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. 
# თქვენი დავალებაა, რომ დააბრუნოთ ამ სიის განახლებული ვერსია, 
# სადაც ყველა სახელი დიდი ასოთი დაიწყება.
listOfNames=["luka","miro","merabi"]
def upperCase(list):
    for i in range (len(list)):
        list[i]=list[i].capitalize()
    return listOfNames
print(upperCase(listOfNames))
print()

#15)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. 
# შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, 
# ახალ სიაში დაამატეთ მისი განაყოფი ორზე, ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. 
# საბოლოოდ დააბრუნეთ განახლებული სია
list1=[23,94,29,10,5]
def oddMultiEvenDiv2(list):
    oddMulti=[]
    evenDiv=[]
    for integer in list:
        if integer%2==0:
            evenDiv.append(integer)
        else:
            oddMulti.append(integer)
    return oddMulti,evenDiv
print(oddMultiEvenDiv2(list1))
print()

#16)შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ 
# ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper). 
string1=("airdot")
string2=("susa")
def reverseAStringUpper(string):
    reverseString=""
    for i in range(len(string)-1,-1,-1):
        reverseString+=string[i].upper()
    return reverseString
print(reverseAStringUpper(string1))
print(reverseAStringUpper(string2))
print()

