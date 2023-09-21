import random


with open("mots.txt", "r") as file:
    lines = file.readlines()

rand_line = random.choice(lines)
words = rand_line.strip().split()
rand_word = random.choice(words)

word=rand_word.lower()
max_attempts = 10
attempts = 0
show_word = "_" * len(word)

while attempts < max_attempts:
    
    guess_letter = input(f"Attempt {attempts}/{max_attempts}: Choose a letter: ")

    found = False  # Variable pour vérifier si une lettre a été trouvée dans cet essai

    for i in range(len(word)):
        if guess_letter == word[i]:
            show_word = show_word[:1*i] + guess_letter + show_word[i+1:]
            found = True  # Une lettre a été trouvée

    print(show_word)

    if show_word == word:
        print("Congratulations, you guessed the word!")
        break

    if not found:
        attempts += 1  # Augmente le nombre d'essais uniquement si aucune lettre n'a été trouvée

if show_word != word:
    print("You've used all your attempts. The word was: ", word)
