#17) შექმენით ფუნქცია, რომელიც იღებს მთელი რიცხვების სიას და 
# აბრუნებს სიაში ყველაზე მცირე რიცხვს.
listNumbers=[4,-6,1,9,19,-32,-8]
def minNumberList(list):
    sortedListNumbers=sorted(listNumbers)
    return sortedListNumbers[0]
print(minNumberList(listNumbers))
print()

#18) შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და 
# აბრუნებს მათ უდიდეს საერთო გამყოფს (GCD-Greatest common divisor).
integerA=24
integerB=60
def gcdIntegers(integer1,integer2):
    x=0
    a=integer1
    while x==0:
        if integer1%a==0 and integer2%a==0:
            x+=1
            return a
        else:
            a-=1
print(gcdIntegers(integerA,integerB))
print()

# 19. შექმენით ფუნქცია, რომელიც იღებს string'ს და 
# აბრუნებს იმავე string'ს uppercase'ში.
# (მაგალითად: input: "Hello World". output: "HELLO WORLD".
string1="Welcome To Europe"
def upperString(string):
    return string.upper()
print(upperString(string1))
print()

# 20. შექმენით ფუნქცია, რომელიც იღებს integer'ების სიას და 
# აბრუნებს მათ საშუალო არითმეტიკულს.
# (მაგალითად: input: [1, 5, 12]. output: (1 + 5 + 12)/3, ანუ 6.) 
# (ელემენტების დასათვლელად გამოიყენეთ ფუნქცია len).
listNumbers=[7,1,8,16,-2]
def avrgNumber(list):
    return sum(list)/len(list)
print(avrgNumber(listNumbers))
