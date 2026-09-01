print("Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numbers.")
    raise SystemExit

print("Choose operation")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print(num1 + num2)
elif choice == "2":
    print(num1 - num2)
elif choice == "3":
    print(num1 * num2)
elif choice == "4":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Please choose 1, 2, 3, or 4")
