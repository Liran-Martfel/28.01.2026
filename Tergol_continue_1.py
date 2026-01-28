i = 0
_max = None
_sum = 0
_neg = 0
while True:
    number = int(input("enter a number: "))
    if number == 0:
        continue
    if number < 0:
        _neg += 1
        continue
    i += 1
    _sum += number
    if number > _max:
        _max = number
    if number % 7 == 0:
        break
print("your sum is:", _sum)
print("your highest is:", _max)
print("you have", _neg, "negative numbers")
print("you have", i, "positive numbers")

