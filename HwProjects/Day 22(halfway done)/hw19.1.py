#7) შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის factorial'ს
def factorial(int):
    factorial=1
    for i in range(1,int+1):
        factorial=factorial*i
    return factorial
print(factorial(5))
print()
#8) შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს 
# და აბრუნებს ორივე list'იდან მაქსიმალური რიცხვების ჯამს.
listOfNumbers1=[1,3,7,4]
listOfNumbers2=[4,15,3,7]
def sumListMaxNumbers(list1,list2):
    newList1=[]
    newList2=[]
    newList1=sorted(list1)
    newList2=sorted(list2)
    return newList1[-1]+newList2[-1]
print(sumListMaxNumbers(listOfNumbers1,listOfNumbers2))
print()

#9) შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და 
# აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას.
listOfNumbers1=[1,3,7,4]
listOfNumbers2=[4,15,3,7]
def subListMinNumbers(list1,list2):
    newList1=[]
    newList2=[]
    newList1=sorted(list1)
    newList2=sorted(list2)
    return newList1[0]-newList2[0]
print(subListMinNumbers(listOfNumbers1,listOfNumbers2))
print()

#10) შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და 
# აბრუნებს ამ სიაში მაქსიმალური და მინიმალური რიცხვების სხვაობას.
listOfNumbers1=[1,3,7,4]
listOfNumbers2=[4,15,3,7]
def subMaxMinNumbers(list1,list2):
    newList1=[]
    newList2=[]
    newList1=sorted(list1)
    newList2=sorted(list2)
    return newList1[-1]-newList2[0]
print(subMaxMinNumbers(listOfNumbers1,listOfNumbers2))
print()

#11) შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს 
# და აბრუნებს ყველა ელემენტის ჯამს.
listOfNumbers=[1,3,18,7,4,10,0]
def sumList(list):
    return sum(list)
print(sumList(listOfNumbers))
print()

#12) შექმენით ფუნქცია, რომელიც იღებს string'ს და 
# აბრუნებს ხმოვანი ასოების რაოდენობას string'ში.
string1="miro"
string2="likely"
string3="suspicious"
string4="yellow"
def vowelAmount(string):
    listOfVowels=["a","e","i","o","u","y"]
    if string[0].lower()=="y":
        listOfVowels.remove("y")
    vowelCount=0
    for char in string:
        if char.lower() in listOfVowels:
            vowelCount+=1
    return vowelCount
print(vowelAmount(string1),end=" ")
print(vowelAmount(string2),end=" ")
print(vowelAmount(string3),end=" ")
print(vowelAmount(string4))

