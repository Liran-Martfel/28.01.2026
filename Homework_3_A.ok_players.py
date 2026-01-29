i = 0
age_16 = 0
counter = 0
while counter < 10:
    age: int = int(input("please enter his age: "))
    if age < 12 or age > 18:
        continue
    else:
        i += 1
        counter += 1
        # I can be used as a counter _but I prefer one that is only for counter
    if age > 16:
        age_16 += 1
print ("the number of good age players is: ", i)
print ("the number of players above 16 is: ", age_16)
