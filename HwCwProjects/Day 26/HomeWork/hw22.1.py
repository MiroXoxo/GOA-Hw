# 11. Print "hi" for each element in a list [1, 2, 3] using a for loop.
for i in [1,2,3]:
    print("hi",end=" ")
print()
# 12. Print "hi" for each element in a list [1, 2, 3] using a while loop.
i=0
while i<len([1,2,3]):
    print("hi",end=" ")
    i+=1
print()
# 13. Print the first 3 positive integers using a for loop.
for i in range(1,4):
    print(i,end=" ")
print()
# 14. Print the first 3 positive integers using a while loop.
i=1
while i<4:
    print(i,end=" ")
    i+=1
print()
# 15. Print the numbers from 1 to 3 in reverse using a for loop.
for i in range(3,0,-1):
    print(i,end=" ")
print()
# 16. Print the numbers from 1 to 3 in reverse using a while loop.
i=3
while i>0:
    print(i,end=" ")
    i-=1
print()
# 17. Print the first 4 letters of the alphabet using a for loop.
for char in "abcd":
    print(char,end=" ")
print()
# 18. Print the first 4 letters of the alphabet using a while loop.
i=0
while i<4:
    print("abcd"[i],end=" ")
    i+=1
print()
# 19. Print the message "looping" 4 times using a for loop.
for i in range(4):
    print("looping",end="...")
print()
# 20. Print the message "looping" 4 times using a while loop.
i=0
while i<4:
    print("looping",end="...")
    i+=1