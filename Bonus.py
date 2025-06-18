number = int(input("Enter a positive integer: "))
while number != abs(number):
    number = int(input("Wrong, Please enter a postivie integer: "))
sum = 0
choose = number
while number > 0:
    if number % 2 == 0:
        sum += number
    number -= 1
print(f"The sum of even numbers between 1 and {choose} is {sum}.")