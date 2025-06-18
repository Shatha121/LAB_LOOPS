# 1)

for number in range(45 , 210):
    if number == 100:
        continue
    elif number == 205:
        break
    print(number)

# 2)
answer = int(input("what is the product of 7 * 24 ? "))
while answer != 168:
    print("Your Answer is wrong try again..")
    answer = int(input("what is the product of 7 * 24 ? "))
else:
    print("You answered this Question correctly")