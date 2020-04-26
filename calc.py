total_points = 100
points_earned = input("Points Earned: ")
grade = (int(points_earned) / total_points) * 100

if grade >= 90 and grade <= 100:
    print(f"Your Grade: {grade}, that's an A!")
elif grade >= 80 and grade < 90:
    print(f"Your Grade: {grade}, that's a B!")
elif grade >= 70 and grade < 80:
    print(f"Your Grade: {grade}, that's a C!")
elif grade >= 101:
    print("Unsupported Entry. Max score of 100.")
else:
    print(f"{grade} You suck...")


def separator():
    print("-" * 30)


def print_menu():
    separator()
    print("Welcome to PyCalc")
    separator()

    print('[1] - Add')
    print('[2] - Subtract')


def sum(num1, num2):
    return num1 + num2


print_menu()
opc = input('Please select an option: ')
print('user input: ' + opc)

num1 = float(input('First Number: '))
num2 = float(input('Second Number: '))
if(opc == '1'):
    res = sum(num1, num2)
    print("Result: " + res)
