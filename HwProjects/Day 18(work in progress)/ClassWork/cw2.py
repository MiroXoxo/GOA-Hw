# 1) შექმენით ისეთი პროგრამა რომელიც 1დან 10მდე გამოითვლის ყველა რიცხვს 
# for loop ის მეშვეობით და თითოეულ რიცხვს 1დან 10მდე დაამატებს სიაში. 
# ციკლის შემდეგ კი გამოიყენეთ len ფუნქცია 
# რატსაა გაიგოთ რამდენი ელემენტისგან შედგება ჩვენი სია
list=[]
for i in range(1,10):
    list.append(i)
print(len(list))
print()

# 2) შექმენით ისეთ პროგრამა რომელიც მომხმარებელს შემოატანინებს 2 რიცხვს. 
# შემოტანის შემდეგ for loop ის მეშვეობით გამოთვალეთ ყველა რიცხვი ამ ორ რიცხვს შორის და 
# შემდეგ ისიდი ჩაამატეთ ლისტში საბოოლოოდ კი დაპრინტეთ ტერმინალში
print("Provide Two Numbers To Print a List Of Integers Between Them")
x=int(input("Input Starting Number: "))
y=int(input("Input The End Number: "))
list=[]
for i in range(x,y+1):
    list.append(i)
if x<=y:
    print(list)
else:
    print("There Is No Integers Between",x,"and",y)
