score = int(input())
total_a = 0
total_b = 0
current_score = 1
while score >=0:
    if current_score %2 ==1:
        total_a+=score
    else:
        total_b+= score
    score = int(input())
    current_score +=1
if total_a < total_b:
    winner= "B"
elif total_a > total_b:
    winner="A"
else:
    winner= "Tie"
print(total_a)
print(total_b)
print(winner)
