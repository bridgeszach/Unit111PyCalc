# total_points = 100
# points_earned = input("Points Earned: ")
# grade = (int(points_earned) / total_points) * 100

# if grade >= 90 and grade <= 100:
#     print(f"Your Grade: {grade}, that's an A!")
# elif grade >= 80 and grade < 90:
#     print(f"Your Grade: {grade}, that's a B!")
# elif grade >= 70 and grade < 80:
#     print(f"Your Grade: {grade}, that's a C!")
# elif grade >= 101:
#     print("Unsupported Entry. Max score of 100.")
# else:
#     print(f"{grade} You suck...")


def separator():
    print("-" * 30)


def print_menu():
    print('\n' * 5)
    separator()
    print("Welcome to PyCalc")
    separator()

    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Close')

    separator()


def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def product(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if(num1 == 0 or num2 == 0):
        res = str(print("NO NO NO!"))
    else:
        num1 / num2


opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    if(opc == 'x'):
        break

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if(opc == '1'):
        res = sum(num1, num2)
        print("Result: " + str(res))
    elif(opc == '2'):
        res = sub(num1, num2)
        print("Result: " + str(res))
    elif(opc == '3'):
        res = product(num1, num2)
        print("Result: " + str(res))
    elif(opc == '4'):
        res = divide(num1, num2)
        print("Result: " + str(res))

    input("Press Enter to Continue...")

print('\n')
print("Goodbye")
