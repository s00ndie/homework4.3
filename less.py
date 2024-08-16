number = int(input("Enter number between 1000 - 9999:"))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number //10 % 10
n4 = number % 10
print(f"{n1} \n{n2} \n{n3} \n{n4}" )