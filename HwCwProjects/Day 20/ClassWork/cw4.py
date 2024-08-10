# 1) შექმენით თქვენი საკუთარი ფუნქცია def keyword გამოყენებით და 
# დაარქვით display_info ფუნქციაში აიღეთ ცვლადი სადაც შეინახავთ 
# თქვენს სახელს შემდეგ მეორე ცვლადს სადაც შეინახავთ გვარს საბოლოოდ 
# მესამე ცვლადი თქვენი ასაკით საბოლოოდ აიღეთ ერთი print ფუნქცია და 
# ყველა ინფორმაცია გამოიტანეთ
def displayInfo(name,surname,age):
    listCategory=["Name: ","Surname: ","Age: "]
    listAnswers=[name,surname,age]
    print("\nINFORMATION")
    for i in range(len(listCategory)):
        print(listCategory[i],listAnswers[i])
displayInfo("miro","gamer",12)
    