speed = int(input())
total_readings= 0
count = 0
longest_streak = 0
while speed >=0:
    total_readings +=1
    if speed <20:
        count +=1
        if count >longest_streak:
            longest_streak = count
        else:
            count = 0 
    speed = int(input())
print(total_readings)
print(longest_streak)
