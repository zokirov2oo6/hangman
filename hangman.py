
import random

stages = [
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

word_list=["bear","lion","camel"]
lives=6
choice = random.choice(word_list)
print(choice)

placeholder=""
word_length = len(choice)
for position in range (word_length):
    placeholder += "_"
print(placeholder)

game_over=False

correct_letters=[]
while not game_over:

    guess=input("Guess a letter: ").lower()
    print(guess)

    display=""
    for letter in choice:
        if letter == guess:
            display += letter
            if guess not in correct_letters:   # <-- TO‘G‘RILANGAN JOY
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choice:
        lives-=1
        if lives == 0:
            game_over=True
            print("You lost!")

    if "_" not in display:
        game_over=True
        print("You win !")

    print(stages[lives])