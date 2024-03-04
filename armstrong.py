print("welcome in armstrong numbers checker")
number = " "
summation=0
# check if it is a valid input
while number.isdigit() is False or int(number) <0:
    number = input("Enter your integer number > 0: ")
power = len(number)
# to save the number
num = int(number)
for i in range(len(number) + 1):
    # take every single digit
    reminder = num % 10
    num //= 10
    summation += (reminder ** power)
# check if the summation of every digit powered with len(number) = to the input number
if summation == int(number):
    print(number, " is an armstrong number")
elif summation != int(number):
    print(number, " isn't an armstrong number")