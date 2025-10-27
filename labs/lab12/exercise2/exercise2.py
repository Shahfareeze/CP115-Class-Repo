score = float(input())

# TODO: Your code here
score_count=0
total_score=0
average_score=0

while score in range (1,100):
    total_score+= score
    score_count+=1
    average_score = total_score/score_count
    score = float(input())

print(score_count)
print(total_score)
print(f"{average_score:.2f}")
