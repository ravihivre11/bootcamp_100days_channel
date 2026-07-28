import random , art 
import dataaa as dt
print(art.logo)
choice_a = random.choice(dt.data)
choice_b = random.choice(dt.data)

while choice_a == choice_b:
    choice_b = random.choice(dt.data)

  
continue_game = True

score = 0


while continue_game:
    print(choice_a['name'])
    print(art.vs)
    print(choice_b['name'])   

    if choice_a["follower_count"] > choice_b["follower_count"]:
        correct_answer = "a"
    else:
        correct_answer = "b"
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choose == correct_answer:
        score += 1
        if correct_answer == "b":
            choice_a = choice_b
        choice_b = random.choice(dt.data)

        while choice_a == choice_b:
           choice_b = random.choice(dt.data)
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
