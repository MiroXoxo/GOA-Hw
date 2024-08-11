# 21. Print the elements of a tuple (1, 2, 3) using a for loop.
for i in (1,2,3):
    print(i,end=" ")
print()
# 22. Print the elements of a tuple (1, 2, 3) using a while loop.
i=0
while i<len((1,2,3)):
    print((1,2,3)[i],end=" ")
    i+=1
print()
# 23. Print the numbers 5, 4, 3, 2, 1 using a for loop.
for i in range(5,0,-1):
    print(i,end=" ")
print()
# 24. Print the numbers 5, 4, 3, 2, 1 using a while loop.
i=5
while i>0:
    print(i,end=" ")
    i-=1
print()
# 25. Print the elements of the list ["apple", "banana", "cherry"] using a for loop.
for i in ["apple", "banana", "cherry"]:
    print(i,end=" ")
print()
# 26. Print the elements of the list ["apple", "banana", "cherry"] using a while loop.
i=0
while i<len(["apple", "banana", "cherry"]):
    print(["apple", "banana", "cherry"][i],end=" ")
    i+=1
print()
# 27. Print the first 3 numbers starting from 0 using a for loop.
for i in range(4):
    print(i,end=" ")
print()
# 28. Print the first 3 numbers starting from 0 using a while loop.
i=0
while i<4:
    print(i,end=" ")
    i+=1
print()
# 29. Print the word "loop" for each number in a list [1, 2, 3, 4] using a for loop.
for i in [1, 2, 3, 4]:
    print("loop",end=" ")
print()
# 30. Print the word "loop" for each number in a list [1, 2, 3, 4] using a while loop.
i=0
while i<len([1, 2, 3, 4]):
    print("loop",end=" ")
    i+=1