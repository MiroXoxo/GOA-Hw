# 1) შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
a=2
def plusFive(number):
    return number+5
print(plusFive(a))
print()

# 2) შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს
a=2
b=5
def multiVariables(multi1,multi2):
    return multi1*multi2
print(multiVariables(a,b))
print()

#3) შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len()).
x="miro"
def lengthString(string):
    return len(string)
print(x,"Strings Length Is",lengthString(x))
print()

# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს 
# და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).
listStrings=["Hello","Welcome","Greetings"]
def lengthList(list):
    lengthListStrings=[]
    for i in list:
        lengthListStrings.append(len(i))
    return lengthListStrings
print(lengthList(listStrings))
print()

# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს 
# თუ ის არის Palindrome 
# (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") 
# და სხვა შემთხვევაში False-ს.
a="deified"
b="palindrome"
c="deed"
d="cool"
def palindrome(string):
    positiveList=[]
    negativeList=[]
    z=-1
    for i in range(0,len(string)//2):
        positiveList.append(string[i])
        negativeList.append(string[z])
        z-=1
    return positiveList==negativeList
print(palindrome(a),palindrome(b),palindrome(c),palindrome(d))
print()

# 6. შექმენით ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში.
listStrings1=["Public","Tonight","Lamp","Daydream","Cigarettes","Remote","Red","Honey"]
listStrings2=["Rice","tree","Copper","Keep","Dark","Moon","Cool","Deputy"]
def maxLenString(list):
    lengthListStrings=[]
    sortedList=[]
    maxStrings=""
    for i in list:
        lengthListStrings.append(len(i))
    sortedList=sorted(lengthListStrings)
    for i in range(len(list)):
          if sortedList[-1]==len(list[i]):
               maxStrings+=(list[i])+" "
    return maxStrings
print(maxLenString(listStrings1))
print(maxLenString(listStrings2))
 

     

