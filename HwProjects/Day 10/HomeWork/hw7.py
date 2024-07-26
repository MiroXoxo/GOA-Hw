# 3)0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი
a=20
for i in range(0,a+1):
    print(i,end=" ")
    if i==20:
        print("\n")

# 4)დაპრინტეთ პირველი 10 ნატურალური რიცხვი
b=10
for x in range(1,b+1):
    print(x,end=" ")
    if x==10:
        print("\n")

# 5)დაპტინტეთ 0-იდან 100-ის ჩათვლით ლუწი რიცხვები
c=100
for y in range(1,c+1):
    if y%2==0:print(y,end=" ")
    if y==100:
        print("\n")
# 6)შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ 
# არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 
number=int(input("Input a Number to Find out if it's value is more or less than 0 or 0: "))
if number>0:
    print("The Inputed Numbers Value Is More Than 0")
elif number==0:
    print("The Inputed Numbers Value Is 0")
else:print("The Inputed Number Value Is Less Than 0")
print("\n")

# 7)შემოატანინეთ მომხმარებელს მისი ასაკი 
# თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” 
# თუ 18 წელზე ნაკლები “you are virgin”
age=int(input("Enter your age: "))
if age >=18:
    print("You are an adult")
else:
    print("You are a virgin")

print("\n")

# 8)დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს 
# მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) 
# გამოიყენეთ if elif else

weekNumber=int(input("Input a Number from 1 to 7 to get the coresponding day of the Week to that Number: "))
if weekNumber==1:print("Monday")
elif weekNumber==2:print("Tuesday")
elif weekNumber==3:print("Wednesday")
elif weekNumber==4:print("Thursday")
elif weekNumber==5:print("Friday")
elif weekNumber==6:print("Saturday")
elif weekNumber==7:print("Sunday")
else:print("You entered an Invalid Charachter or a Number not corresponding to any days of the week")



  

