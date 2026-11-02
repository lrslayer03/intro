
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = max(num1, num2)

while True:
    if largest % num1 == 0 and largest % num2 == 0:
        print("LCM is:", largest)
        break
    largest = largest + 1