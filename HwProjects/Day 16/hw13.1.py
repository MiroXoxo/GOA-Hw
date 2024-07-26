#4) მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, საცხოვრებელი ადგილი და მეილი. 
# ყველა შეინახეთ ცვლადებში და შემდეგ ჩაამატეთ სიაში, საბოლოოდ კი დაბეჭდეთ ეს სია.
listCategory=["Name: ","Surname: ","Living Residence: ","E-mail: "]
listAnswers=[]
print("Fill Out The Information")
for i in range(0,len(listCategory)):
    listAnswers.append(input(listCategory[i]))
print("\nINFORMATION")
for i in range(len(listCategory)):
    print(listCategory[i],listAnswers[i])
print()

#5) ცვლადში შეინახეთ თქვენი გვარი. 
# გამოიყენეთ indexing და მისი თითოეული ასო დაბეჭდეთ.
surname="Alalidze"
for i in surname:
    print(i,end=" ")