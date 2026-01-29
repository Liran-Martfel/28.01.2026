x: int = 1
i = 1
while True:
    number = int(input("Enter a number: "))
    if number > x:
        x = number
        i += 1
        if i == 4:
            break
    else:
        i = 1
        x = 1

