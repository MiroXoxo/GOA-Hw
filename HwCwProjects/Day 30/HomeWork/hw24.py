# 3) შექმენით ფუნქცია სახელად odd_index_sum რომელსაც გადაეცემა რიცხვების სია, 
# თქენი დავალებაა შეკრიბოთ ყველა ის რიცხვი რომელიც დგას !!!!კენტ ინდექსზე!!!, 
# მიღებული ჯამი დააბრუნეთ ფუნქციიდან
def oddIndexSum(list):
    sumOdd=0
    for i in range(len(list)):
        if i%2!=0:
            sumOdd=sumOdd+list[i]
    return sumOdd
print(oddIndexSum([231,2,45,1,-24,0,11,22]))
