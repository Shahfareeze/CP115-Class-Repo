
# Find the type of average score

score1 = 85
score2 = 92.5
score3 = 78

score2 = int(score2)
score3 = float(score3)

print(type(score2))
print(type(score3))

average_score = (score1 + score2 + score3 ) / 3

print(f"Average Score = {average_score} (type: {type(average_score)})")

#Change to Int type.
average_score_int = int(average_score)

print(f"(type: {type(average_score_int)})")

#Next exercise

result1 = score1 ** 2 / score2 + score3 % 7
print(f"Result 1 = {result1} (type: {type(result1)})")

# Question 5


