lower: int = int(input("Enter number: "))
while True:
    higher: int = int(input("Enter higher number: "))
    if higher <= lower:
        lower = int(input("Enter new number: "))
        continue
    if higher > lower:
        break
for i in range (lower,higher + 1):
    print(i)