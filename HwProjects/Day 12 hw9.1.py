# 6)დაწერეთ ალგორითმი რომელიც ბეჭდავს 5-ის ჯერად რიცხვებს 
# (რიცხვები რომლებიც იყოფა 5-ზე) 1-დან 50-ის ჩათვლით
a=1
while a<=50:
    if a%5==0:print(a,end=" ")
    a=a+1
#or
# a=5
# while a<=50:
#     print(a)
#     a=a+5
print("\n")

# 7)მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვი. 
# შემდეგ შეამოწმეთ რომელია უდიდესი და გამოიყენეთ for ციკლი: 
# უმცირესიდან უდიდესამდე დაპრინტეთ ყველა რიცხვი
list=[]
print("Input Two Numbers To Sort From Low To High Value",)
for a in range(2):
    if a<1:print("First Number:",end=" ")
    else:print("Second Number:",end=" ")
    listValue=int(input())
    list.append(listValue)
list.sort()
b=0
while b<2:
    print(list[b],end=" ")
    b=b+1
print("\n")

# 8) გადაიმეორეთ განვლილი მასალა და გააკეთეთ მაგალითები

# 9)დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 
# 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.
multi=1
for i in range(5,11):
     multi=multi*i
print(multi)