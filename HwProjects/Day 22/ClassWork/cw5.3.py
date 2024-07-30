#15)შექმენით ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების სიას და 
# აბრუნებს სიაში ყველა რიცხვის ჯამს.
print("Input Numbers To Get The Sum Of Them\nFor Adding Input +\nTo Get The Sum Input =")
sumList=[]
x="+"
while x=="+":
    sumList.append(float(input("Number: ")))
    x=input("+ or =\n")
if x=="=":
    sum=str(sum(sumList))
    while sum[-1]=="0" or sum[-1]==".":
        sum=sum[:-1]
    print("The Sum Of The Numbers Is:",sum)
else:
    print("You Entered An Incorrect Input Try Again")

     
    