# Busog, Kenneth Brian
# Taller, John Amiel

import random
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return  x * y

def dividiby(x, y):
    return x / y

def total_result(total, correct):
    print("Problem number: ", total, "\n","Correct Answer: ", correct)

title = "* Math Tutor v2.0 *"
print("*" * len(title))
print(title)
print("*" * len(title))

list = ["1 - Addition", "2 - Subtraction", "3 - Multiplication", "4 - Division"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

print("-" * 19)

while True:
    choice = input("Choose Operation: ")
    num_choice = input("How many problems: ")
    j = 0
    count = 0
    if choice in ('1', '2', '3','4'):
        if choice == '1':
            while j < int(num_choice):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("correct")
                    print("-" * 19)
                    count += 1
                else:
                    print("Wrong! the correct answer is " + str(num3))
                    print("-" * 19)
                j += 1

        elif choice == '2':
            while j < int(num_choice):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtract(num1, num2)
                print("What is the difference of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("correct")
                    print("-" * 19)
                    count += 1
                else:
                    print("Wrong! the correct answer is " + str(num3))
                    print("-" * 19)
                j += 1

        elif choice == '3':
            while j < int(num_choice):
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the product of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("correct")
                    print("-" * 19)
                    count += 1
                else:
                    print("Wrong! the correct answer is " + str(num3))
                    print("-" * 19)
                j += 1

        elif choice == '4':
            while j < int(num_choice):
                num1 = round(float(random.randint(0, 9)))
                num2 = round(float(random.randrange(2, 10, 2)))
                num3 = dividiby(num1, num2)
                print("What is the quotient of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("correct")
                    print("-" * 19)
                    count += 1
                else:
                    print("Wrong! the correct answer is " + str(num3))
                    print("-" * 19)
                j += 1
        print(f"Score: {count} / {num_choice}")

        percentage = (int(count) / int(num_choice)) * 100
        if percentage < 75:
            print(f"You've got {percentage}%. Better luck next time!")
        elif percentage == 75:
            print(f"You've got {percentage}%. Just a little more practice!")
        else:
            print(f"You've got {percentage}%. Congratulation!!")
        print("-" * 19)

        try_again = input("want to try again? (yes/no): ")
        if try_again == "no":
            print("Thank you for using our Program :)")
            break
        elif try_again == "yes":
            print("GOODLUCK!!")
            print("-" * 19)
            j = 0
            count = 0
        else:
            print("Invalid Input")

