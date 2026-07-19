minutesBefore = float(input())
membership = input()
if minutesBefore < 0:
    price = 0
else:
    if minutesBefore > 0.3:
        price = 80 - 15
        if membership == "yes":
            price = price * 0.15
    else:
        price = 80
print(price)
