#13) შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს 
# და აბრუნებს ახალ list'ს თითოეული integer'ის კვადრატით. 
# (მაგალითად: input: [2, 4]. output: [4, 16])
listOfNumbers=[4,7,6,1,3,-5]
def quadList(list):
    quadListOfNumbers=[]
    for i in range(len(listOfNumbers)):
        quadListOfNumbers.append(listOfNumbers[i]*listOfNumbers[i])
    return quadListOfNumbers
print(quadList(listOfNumbers))
print()

# 14. შექმენით ფუნქცია, რომელიც 
# იღებს string's და აბრუნებს მის შებრუნებულს.
string1="todria"
string2="miro"
def reverseAString(string):
    reverseString=""
    for i in range(len(string)-1,-1,-1):
        reverseString+=string[i]
    return reverseString
print(reverseAString(string1))
print(reverseAString(string2))
print()

# 15. შექმენით ფუნქცია, რომელიც იღებს რაიმე integer'ს და 
# თუ ლუწია აბრუნებს True'ს, თუ კენტი False'ს.
integer1=6
integer2=3
integer3=0
def evenInt(integer):
    return integer%2==0
print(evenInt(integer1),end=" ")
print(evenInt(integer2),end=" ")
print(evenInt(integer3))
print()

listStrings1=["Cash","Post","Office","Fire","Department","Meet","Sea","Maple"]
listStrings2=["A","B","C","D","E","FG","H","IJ"]
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

