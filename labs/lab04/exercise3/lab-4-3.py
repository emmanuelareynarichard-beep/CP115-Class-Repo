hours = int(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours > 5:
        parkingFee = 6.0 + hours - 5 * 3.0
    else:
        parkingFee = hours - 2 * 2.0
if parkingFee > 30.0:
    parkingFee = 30.0
print(parkingFee)
