# 1) შექმენით სია, სადაც შეიტანთ თქვენი ოჯახის წევრების სახელებს. 
# გამოიყენეთ indexing და დაბეჭდეთ ყველას სახელი ცალ-ცალკე.
list=["Mari","Elene","Natali","Tako","Nunuka"]
for i in list:
    print(i,end=" ")
print("\n")

# 2) ექმენით სია, სადაც გექნებათ 1-იდან 10-ის ჩათვლით რიცხვები. 
# ჯერ გამოიტანეთ სიის პირველი, ხოლო შემდეგ ბოლო ელემენტი.
list=[1,2,3,4,5,6,7,8,9,10]
print(list [0],list[-1])
print("\n")

# 3) შექმენით სია, სადაც გექნებათ 10-იდან 20-ის ჩათვლით რიცხვები.
#  გაიხსენეთ ის ფაქტი, რომ თქვენ შეგიძლიათ უკვე შექმნილი სიის ელემენტების შეცვლა
# შეცვალეთ სიის ლუწ ინდექსებზე მყოფი ელემენტები და მათ მაგივრად დაწერეთ 1.
list=[10,11,12,13,14,15,16,17,18,19,20]
for i in range(0,len(list)):
    if i%2==0:
        list[i]=1
print(list)




