number = 0
for number in range (1,100):
    while number <100:
        if number%7 ==0 and number%13 == 0:
            found_number=number
            break
        else:
            number+=1
            print(f"Right now is {number}:")
print(found_number)
