#გაიარეთ while ციკლები და გააკეთეტ 5 მაგალითი while ციკლზე (თქვენ მოიფიქრეთ)
#1)
a=1
while a<11:
    print(a,end=" ")
    a=a+1
print("\n")

#2)
b=10
while b>0:
    print(b,end=" ")
    b=b-1
print("\n")

#3)
c=int(input("Input a Number You To Find Out it's Factorial: "))
d=0
factorial=1
while d<c:
    d=d+1
    factorial=factorial*d
print(factorial)
print("\n")

#4)
print("Input A String And The Number Of Times You Want It Printed")
string=input("String: ")
y=int(input("Number Of Times To Print: "))
x=0
while y>0 and y>x :
    print(string,end=" ")
    x+=1
