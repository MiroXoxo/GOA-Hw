#16)დაწერეთ ფუნქცია, რომელიც იღებს სტრიქონს და ითვლის ხმოვანთა 
# რაოდენობას (a, e, i, o, u) სტრიქონში.
def vowelCountInString(string):
    vowelCount=0
    listOfVowels=["a","e","i","o","u"]
    for char in string:
        if char.lower() in listOfVowels:
            vowelCount+=1
    return vowelCount
print(vowelCountInString("This Is A String And Has Eleven Vowels"))
print()

# 17. განსაზღვრეთ ფუნქცია, რომელიც იღებს სტრიქონების ჩამონათვალს და 
# აბრუნებს ახალ სიას ყველა სტრიქონის დიდი ასოებით.
listOfStrings=["Random String","United States Of America","GOOD HEAVENS!"]
listOfUppercase=[]
def onlyUppercase(listStrings):
    for i in range(len(listOfStrings)):
     
        for char in listStrings[i]:
            if char.isupper():
                listOfUppercase.append(char)
    return listOfUppercase
print(onlyUppercase(listOfStrings))
 
