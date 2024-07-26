# 2) შექმენით ფუნქცია hello() სადაც print ფუნქციის გამოყენებით გამოიტანთ  "GOA Best!"
def hello():
    print("GOA Is The Best!")
hello()
print()

# 3) შექმენით ფუნქცია sum რომელიც მიიღებს ორ არგუმენთ მაგ: 
# a , b  და შემდეგ print-ის გამოყენებით გამოიტანთ მათ ჯამს
a=5
b=2
def sum():
    print(a+b)
sum()
print()

# 4) შექმენით ფუნქცია to_string რომელიც მიიღებს ერთ არგუმენტს მაგალითად 
# value  რომელსაც დაბეჭდავთ სტრინგად str-ის გამოყენებით
x=465
def toString(value):
    print(str(value))
toString(x)
print()

# 5) შექმენით ფუნქცია print_type რომელიც მიიღებს ერთ არგუმენტს და შემდეგ 
# built-in function  type() გამოყებით შეამოწმებთ მის მონაცემთა ტიპს და გამოიტანთ ეკრანზე
z="miro"
x=234
a=[1,2,3]
def printType(variable):
    print(variable,"is a",type(variable))
printType(z)
printType(x)
printType(a)
print()

# 6) შექმენთ ფუნქცია to_integer რომელიც მიიღებს ერთ არგუმენტს მაგალითად 
# value ისევ და შემდეგ print-ის გამოყენებით გამოიტანეთ ინტეჯერად int ფუნქციით
b="567"
def toInteger(value):
    print(int(value))
toInteger(b)

