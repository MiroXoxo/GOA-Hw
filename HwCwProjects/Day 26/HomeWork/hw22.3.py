# 31. Print the characters of the string "abc" using a for loop.
for char in "abc":
    print(char,end=" ")
print()
# 32. Print the characters of the string "abc" using a while loop.
i=0
while i<len("abc"):
    print("abc"[i],end=" ")
    i+=1
print()
# 33. Print the first 2 elements of a list ["x", "y", "z"] using a for loop.
for i in range(2):
    print(["x", "y", "z"][i],end=" ")
print()
# 34. Print the first 2 elements of a list ["x", "y", "z"] using a while loop.
i=0
while i<2:
    print(["x", "y", "z"][i],end=" ")
    i+=1
print()
# 35. Print the message "Hello World" 2 times using a for loop.
for i in range(2):
    print("Hello World",end="  ")
print()
# 36. Print the message "Hello World" 2 times using a while loop.
i=0
while i<2:
    print("Hello World",end="  ")
    i+=1
print()
# 37. Print the elements of a set {1, 2, 3} using a for loop.
for elements in {1, 2, 3}:
    print(elements,end=" ")
print()
# 38. Print the elements of a set {1, 2, 3} using a while loop.
i=0
while i<len({1, 2, 3}):
    print(list({1, 2, 3})[i],end=" ")
    i+=1
print()
# 39. Print the elements of the dictionary {"a": 1, "b": 2} using a for loop.
for char,num in {"a": 1, "b": 2}.items():
    print(char,num,end=" ")
print()
# 40. Print the elements of the dictionary {"a": 1, "b": 2} using a while loop.
dictionary={"a": 1, "b": 2}
i=0
while i<len(dictionary):
    print(list(dictionary)[i],end=" ")
    print(dictionary[list(dictionary)[i]],end=" ")
    i+=1
