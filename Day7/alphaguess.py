import random
list = ["ravi" , "nilesh", "kartik"]
lives = 6
word = random.choice(list)
print(word)

placeholder= ""
for position in range(1,len(word)+1):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:
    print(f"You have {lives}/6 lives left")
    guess = input("Guess the word:").lower()

    if guess in correct_letter:
        print(f"You have already guessed {guess}")
        continue

    display =""

    for letter in word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"********The correct word was{word} You lose********")
    
    if "_" not in display:
        game_over = True
        print("********You win********")

    # print(stages[lives])    
