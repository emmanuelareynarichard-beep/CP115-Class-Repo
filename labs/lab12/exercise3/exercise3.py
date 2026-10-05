grade = float(input())
valid_count = 0
total = 0 
while grade!=-1:
    if grade <0 or grade>100:
        print("Invalid number,skip")
        grade = float(input())
        continue
    else:
        valid_count +=1
        total+=grade
        average = total/valid_count
        grade = float(input())

print(valid_count)
print(f"{average:.2f}")
