import tkinter as tk
import random

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StickMan")

        self.canvas = tk.Canvas(self.root, width=100, height=150)
        self.canvas.pack()

        self.attempts = 0
        self.max_attempts = 10
        self.show_word = ""

        self.body_parts = [
            # base
            lambda : self.canvas.create_line(20, 80, 60, 80, fill="black", width=4),
            # poteau
            lambda : self.canvas.create_line(40, 20, 40, 80, fill="black", width=4),
            # barre du haut
            lambda : self.canvas.create_line(20, 20, 80, 20, fill="black", width=4),
            # diagonale
            lambda : self.canvas.create_line(40, 30, 60, 20, fill="black", width=4),
            # corde
            lambda : self.canvas.create_line(65, 20, 65, 25, fill="black", width=2),
            # torse
            lambda : self.canvas.create_line(65, 30, 65, 60, fill="black", width=2),
            # bras
            lambda : self.canvas.create_line(50, 50, 80, 50, fill="black", width=2),
            # jambre gauche
            lambda : self.canvas.create_line(50, 75, 65, 60, fill="black", width=2),
            # jambre droite
            lambda : self.canvas.create_line(80, 75, 65, 60, fill="black", width=2),
            # tête
            lambda : self.canvas.create_oval(60, 25, 70, 40, fill="black")
        ]

        self.body_parts_drawn = [False] * len(self.body_parts)

        self.play_hangman()

    def update_drawing(self):
        if self.attempts > 0:
            # Vérifiez si la partie du bonhomme de bâton n'a pas déjà été dessinée
            if not self.body_parts_drawn[self.attempts - 1]:
                self.body_parts[self.attempts - 1]()  # Exécute la fonction lambda pour dessiner la partie
                self.body_parts_drawn[self.attempts - 1] = True  # Marque la partie comme dessinée

    def play_hangman(self):
        with open("mots.txt", "r") as file:
            lines = file.readlines()

        rand_line = random.choice(lines)
        words = rand_line.strip().split()
        rand_word = random.choice(words)

        word = rand_word.lower()
        self.show_word = "_" * len(word)

        while self.attempts < self.max_attempts:
            guess_letter = input(f"Attempt {self.attempts}/{self.max_attempts}: Choose a letter: ")

            found = False  # Variable pour vérifier si une lettre a été trouvée dans cet essai

            for i in range(len(word)):
                if guess_letter == word[i]:
                    self.show_word = self.show_word[:i] + guess_letter + self.show_word[i + 1:]
                    found = True  # Une lettre a été trouvée

            print(self.show_word)

            if self.show_word == word:
                print("Congratulations, you guessed the word!")
                break

            if not found:
                self.attempts += 1  # Augmente le nombre d'essais uniquement si aucune lettre n'a été trouvée

            # Planifier une mise à jour du dessin après chaque essai
            self.root.after(1000, self.update_drawing)

        if self.show_word != word:
            print("You've used all your attempts. The word was: ", word)

        # Fermer la fenêtre graphique lorsque le jeu est terminé
        # self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
