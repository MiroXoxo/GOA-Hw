# 6)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგები და ინტეჯერები რაღაც თანმიმდევრობით. 
# ფუნქციამ უნდა შეძლოს და ეს სტრინგების და ინტეჯერების თანმიმდევრობა უნდა გამოიტანოს 
# შებრუნებულად.
def reverseList(list):
    reversedList=[]
    for i in range(len(list)-1,-1,-1):
        reversedList.append(list[i])
    return reversedList
print(reverseList([5,"Apple",28,"Horse",-3,"T-Rex",553,"Train"]))
print()

# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი. 
# ამ ფუნქციამ უნდა იპოვოს ყველაზე გრძელი და ყველაზე მოკლე სტრინგები ამ ლისტში.
listStrings1=["Cash","Post","Office","Fire","Department","Meet","Sea","Maple"]
listStrings2=["A","B","C","D","E","FG","H","IJ"]
def maxMinLenString(list):
    lengthListStrings=[]
    sortedList=[]
    maxStrings=""
    minStrings=""
    for i in list:
        lengthListStrings.append(len(i))
    sortedList=sorted(lengthListStrings)
    for i in range(len(list)):
          if sortedList[-1]==len(list[i]):
               maxStrings+=(list[i])+" "
    for i in range(len(list)):
          if sortedList[1]==len(list[i]):
               minStrings+=(list[i])+" "
    return f"Maximum Length:  {maxStrings}\nMinimum Lenghth: {minStrings}"
print(maxMinLenString(listStrings1))
print()
print(maxMinLenString(listStrings2))
print()

#8) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე სტრინგი. 
# ამ ფუნქციამ უნდა შეძლოს და თითოეული ასო შეცვალოს 
# (პატარა ასო დიდი ასოთ a-A ხოლო დიდი ასო პატარათი A-a).
def reverseCase(string):
    reversedCase=""
    for char in string:
        if char.isupper():
            reversedCase=reversedCase+char.lower()
        elif char.islower():
            reversedCase=reversedCase+char.upper()
        else:
            reversedCase=reversedCase+char
    return reversedCase
print(reverseCase("1 2 3 Go"))
print(reverseCase("REVERSE case")) 
