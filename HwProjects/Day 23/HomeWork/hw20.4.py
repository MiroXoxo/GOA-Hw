#17)შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> 
# (["dato" , "nika" , "polieqtori" , "zaza"....)], 
# დამატებით შექმენით ორი სია odd = [] და even = [], 
# გადაუარეთ ორიგინალ სიას for ციკლით და გაიგეთ რომელი 
# ელემენტი შედგება კენტი ასოებისგან და რომელი ლუწი, საბოლოოდ ჩაამატეთ 
# შესაბამისი სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ.
list1=["dato","nika" ,"polieqtori", "zaza","gocha","miriani","asa","lio"]
evenC=[]
oddC=[]
def SortLenCapitilize(list):
    for string in list:
        if len(string)%2==0:
            evenC.append(string.upper())
        else:
            oddC.append(string.upper())
SortLenCapitilize(list1)
print(evenC,"\n",oddC)
print()

#18)შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან, 
# გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა არის ლუწი, 
# ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში და გადააკეთეთ იგი upper ფუნქციით, 
# თუ იქნება ამ სტრინგის ასოების რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც 
# პირველი character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია. 
list1=["dato","nika" ,"polieqtori", "zaza","gocha","miriani","asa","lio"]
def sortC(list):
    sortedCList=[]
    for string in list:
        if len(string)%2==0:
            sortedCList.append(string.upper())
        else:
            sortedCList.append(string[0].upper()+string[1:])
    return sortedCList
print(sortC(list1))
print()

#19)შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი ყველანაირი სტრინგისგან 
# (დიდი ასოებით / პატარა ასოებით : "dato" , "LUKA") , 
# გადაურეთ ამ სიას და თუ ეს კონკრეტული ელემენტი არის შემდგარი დიდი ასოებისგან, 
# დაამატეთ სიაში ისე როგორც lower, ხოლო თუ შედგება პატარა ასოებისგან 
# დაამატეთ სიაში ისე როგორც upper / !HINT : გადახედეთ ფუნქციებს, isupper() და islower()! 
list1=["dato","NIKA","polieqtori", "zaza","GICHA","miriani","ASA","LIO"]
def reverseC(list):
    upperC=[]
    lowerC=[]
    for string in list:
        if string.isupper():
            lowerC.append(string.lower())
        else:
            upperC.append(string.upper())
    return upperC,lowerC
print(reverseC(list1))
print()

#20)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი, 
# ამ სტრინგზე გამოიყენეთ find() ფუნქცია და თუ find ფუნქცია დააბრუნებს ლუწ ინდექს მაშინ 
# ეს სტრინგი დააბრუნეთ დიდი ასოებით (upper) ხოლო თუ დააბრუნებს კენტ ინდექსს, 
# მაშინ დააბრუნეთ ეს სტრინგი რომლის პირველი ასოც იქნება დიდი (capitalize) 
string1="miro"
def findString(string,stringToFind):
    if string.find(stringToFind)%2==0:
        return stringToFind.upper()
    else:
        return stringToFind.lower()
print(findString(string1,"m"))
print(findString(string1,"o"))
