while True:
    binary = input("Enter your Binary (or q to quit): ")

    if binary.lower() == "q":
        print("Program ended.")
        break

    if not binary or any(digit not in "01" for digit in binary):
        print("Please enter only 0s and 1s.")
    else:
        decimal = int(binary, 2)
        print("Decimal :", decimal)
        print()