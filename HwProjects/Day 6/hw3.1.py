 # 5. მომხმარებელს შემოატანინეთ ორი რიცხვი.
# თქვენი დავალებაა შექმნათ კალკულატორი, დაბეჭდეთ: რიცხვების
# ჯამი (num1 + num2),
# სხვაობა (num1 - num2),
# ნამრავლი (num1 * num2),
# განაყოფი (num1 / num2)
print("CALCULATOR")
print("Here are the list of avalable operations\nInput the prefered operation to perform on two numbers:")
print("+ "," - "," * "," /", "//")

operation=input("Choose operation: ")
a=int(input("Input the First Number: "))
b=int(input("Input the Second Number: "))

sum=a+b
sub=a-b
mult=a*b
div_float=a/b
div = a//b

if operation=="+":
     print(sum)
elif operation=="-":
     print(sub)
elif operation=="*":
     print(mult)
elif operation=="/":
     print(div)
else:
     print("Invalid input please try again and only choose from the following Operations")