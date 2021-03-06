lim = int(input("Enter range : "))
print("Prime numbers are :")
for i in range(lim):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            print(i)
