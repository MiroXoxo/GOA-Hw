# 2) გამოიტანეთ რიცხვები 0-დან 20-ის ჩათვლით
a=20
for i in range(0,a+1):
     print(i,end=" ")
print("\n")

# 3)მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ შემოტანილი რიცხვი 
# ლუწია თუ არა თუ ლუწია დაუპრინტეთ "Number is even"
b=int(input("Input a Number too find out if it's Even or Odd: "))
if b%2==0:print("The Number",b,"is Even")
else:print("The Number",b,"is Odd")

# 4) დაპრინტეთ 20-მდე ლუწი რიცხვები
c=20
for i in range(1,c+1):
    if i%2==0:print(i,end=" ")
print("\n")
# 5)50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ 
# for ციკლის გამოყენებით. ეს ჯამი უნდა შეინახოს ცვლადში, 
# ამიტომ ციკლის გარეთ შექმენით sum ცვლადი (sum-ჯამი) 
sum=0
for i in range(50,101):
     sum=sum+i
print(sum)
   

