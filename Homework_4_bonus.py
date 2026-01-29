x: int = 1
i = 0
while True:
    number = int(input("Enter a number: "))
    if number > x:
        x = number
        i += 1
        if i == 3:
            break
    else:
        i = 0
        x = 1
