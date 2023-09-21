import tkinter as tk
import random
import threading
import time
import queue

# create the function to draw teh stick man
def draw_stickman(canvas):
    # body
    # base
    canvas.create_line(20, 80, 60, 80, fill="black", width=4)
    # poteau
    canvas.create_line(40, 20, 40, 80, fill="black", width=4)
    # barre du haut
    canvas.create_line(20, 20, 80, 20, fill="black", width=4)
    # diagonale
    canvas.create_line(40, 30, 60, 20, fill="black", width=4)
    # corde
    canvas.create_line(65, 20, 65, 25, fill="black", width=2)
    # torse
    canvas.create_line(65, 30, 65, 60, fill="black", width=2)
    # bras
    canvas.create_line(50, 50, 80, 50, fill="black", width=2)
    # jambre gauche
    canvas.create_line(50, 75, 65, 60, fill="black", width=2)
    # jambre droite
    canvas.create_line(80, 75, 65, 60, fill="black", width=2)
    # tête
    canvas.create_oval(60, 25, 70, 40, fill="black")


# Fonction pour mettre à jour le dessin en fonction des échecs
def update_drawing():
    global attempts, canvas 
    max_attempts = 10
    while attempts < max_attempts:
        time.sleep(1)  # Attendre 1 seconde entre les mises à jour du dessin
        if attempts > 0:
            root.after(0, body_parts[attempts - 1])  # Planifier la mise à jour dans le thread principal
        time.sleep(1)  # Attendre 1 seconde avant de continuer


def play_hangman():
    global attempts, show_word
    with open("mots.txt", "r") as file:
        lines = file.readlines()

    rand_line = random.choice(lines)
    words = rand_line.strip().split()
    rand_word = random.choice(words)

    word=rand_word.lower()
    max_attempts = 10
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

     # Fermer la fenêtre graphique lorsque le jeu est terminé
    root.destroy()

attempts = 0

# Define a list of body parts to draw
body_parts = [
    # base
    lambda : canvas.create_line(20, 80, 60, 80, fill="black", width=4),
    # poteau
    lambda : canvas.create_line(40, 20, 40, 80, fill="black", width=4),
    # barre du haut
    lambda : canvas.create_line(20, 20, 80, 20, fill="black", width=4),
    # diagonale
    lambda : canvas.create_line(40, 30, 60, 20, fill="black", width=4),
    # corde
    lambda : canvas.create_line(65, 20, 65, 25, fill="black", width=2),
    # torse
    lambda : canvas.create_line(65, 30, 65, 60, fill="black", width=2),
    # bras
    lambda : canvas.create_line(50, 50, 80, 50, fill="black", width=2),
    # jambre gauche
    lambda : canvas.create_line(50, 75, 65, 60, fill="black", width=2),
    # jambre droite
    lambda : canvas.create_line(80, 75, 65, 60, fill="black", width=2),
    # tête
    lambda : canvas.create_oval(60, 25, 70, 40, fill="black")
]

# Create the main window
root = tk.Tk()
root.title("StickMan")

# create the canvas
canvas= tk.Canvas(root, width=100, height=150)
canvas.pack()

# Créer une file d'attente pour la mise à jour du dessin
update_queue = queue.Queue()

# Démarrer un thread pour mettre à jour le dessin
drawing_thread = threading.Thread(target=update_drawing, args=(update_queue,))
drawing_thread.start()

# Exécuter le jeu du pendu dans le thread principal
play_hangman()

# Exécuter la mise à jour du dessin depuis le thread principal
while True:
    try:
        update_function = update_queue.get_nowait()
        update_function()
    except queue.Empty:
        break

# excute the loop
root.mainloop()

