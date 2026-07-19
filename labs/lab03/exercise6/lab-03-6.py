yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
yardArea = yardLength * yardWidth
houseArea = houseLength * houseWidth
wage = yardArea - houseArea * 2.0
print(wage)
