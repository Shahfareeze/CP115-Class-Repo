num_rounds = int(input())

# TODO: Your code here
# Use input() inside the loop to get each round's score
final_score = 0 
rounds_processed = 0

for rounds_processed in range (num_rounds):
    round_score = int(input())

    if round_score > 100:
        bonus_score = (round_score * 0.2) 
        final_score += bonus_score


    final_score += round_score
    rounds_processed += 1


print(f"{final_score:.1f}")
print(rounds_processed)