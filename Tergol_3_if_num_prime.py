number: int = int(input("enter a number: "))
i: int = 2
while True:
    if number == 2:
        print("the number is a prime number")
        break
    if number % 2 == 0 or number % i == 0 or number == 1:
        print("the number isn't a prime number")
        break
    if number % i != 0:
        i += 1
        if number == i:
            print ("the number is a prime number")
            break

