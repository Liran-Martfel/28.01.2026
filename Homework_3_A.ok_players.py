i = 0
age_16 = 0
z = 0
while z < 10:
    age: int = int(input("please enter his age: "))
    if age < 12:
        continue
    elif age > 18:
        continue
    else:
        i += 1
        z += 1
    if age >= 16:
        age_16 += 1
print ("the number of good age players is: ", i)
print ("the number of players above 16 is: ", age_16)
print ("you have total of: ", i+age_16, "players")
