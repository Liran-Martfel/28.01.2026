total_price = 0
i = 0
while True:
    product: int = int(input("Enter a price: "))
    total_price = total_price + product
    i = i + 1
    if total_price >= 1000:
        break
print("your total is: ", total_price)
print("you bought", i ,"items")