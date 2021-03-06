num = temp = int(input("Enter number: "))
sum = 0
while num > 0:
    rem = num % 10
    sum += rem ** 3
    num = num // 10
if sum == temp:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRONG")
