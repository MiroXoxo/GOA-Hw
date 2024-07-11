# 10)BOSS: For loop დახმარებით ეცადეთ, 
# რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით 
# (შეიძლება არ გამოგივიდეთ მაგრამ სცადეთ)
word=input("Input a Word To Reverse It: ")
for a in range(len(word)-1,-1,-1):
    print(word[a],end="")

print()

b=len(word)-1
while b>=0:
    print(word[b],end="")
    b=b-1

print()

reversedWord=""
for c in range (0,len(word)):
    reversedWord=word[c]+reversedWord
print(reversedWord)