# 41. Print the numbers 10, 20, 30 using a for loop.
for i in range(3):
    print((i+1)*10,end=" ")
print()
# 42. Print the numbers 10, 20, 30 using a while loop.
i=1
while i<4:
    print(i*10,end=" ")
    i+=1
print()
# 43. Print "Done" after completing a for loop.
for i in range(5):
    print("Looping",end="...")
print("\nDone")
# 44. Print "Done" after completing a while loop.
i=0
while i<5:
    print("Looping",end="...")
    i+=1
print("\nDone")
# 45. Print the elements of a nested list [[1, 2], [3, 4]] using a for loop.
for nest in [[1, 2], [3, 4]]:
    for char in nest:
        print(char,end=" ")
print()
# 46. Print the elements of a nested list [[1, 2], [3, 4]] using a while loop.
a=0
b=0
while a<len([[1, 2], [3, 4]]):
    while b<len([[1, 2], [3, 4]][a]):
        print([[1, 2], [3, 4]][a][b],end=" ")
        b+=1
    b=0
    a+=1
print()
# 47. Print the first 5 positive integers using a for loop.
for i in range(1,6):
    print(i,end=" ")
print()
# 48. Print the first 5 positive integers using a while loop.
i=1
while i<6:
    print(i,end=" ")
    i+=1
print()    
# 49. Print each character of the string "loop" using a for loop.
for char in "loop":
    print(char,end=" ")
print()
# 50. Print each character of the string "loop" using a while loop.
i=0
while i<len("loop"):
    print("loop"[i],end=" ")
    i+=1