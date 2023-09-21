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
        self.word = ""

        self.game_started = False  # Variable pour suivre si le jeu a commencé

        self.body_parts = [
            # base
            lambda: self.canvas.create_line(20, 80, 60, 80, fill="black", width=4),
            # poteau
            lambda: self.canvas.create_line(40, 20, 40, 80, fill="black", width=4),
            # barre du haut
            lambda: self.canvas.create_line(20, 20, 80, 20, fill="black", width=4),
            # diagonale
            lambda: self.canvas.create_line(40, 30, 60, 20, fill="black", width=4),
            # corde
            lambda: self.canvas.create_line(65, 20, 65, 25, fill="black", width=2),
            # torse
            lambda: self.canvas.create_line(65, 30, 65, 60, fill="black", width=2),
            # bras
            lambda: self.canvas.create_line(50, 50, 80, 50, fill="black", width=2),
            # jambre gauche
            lambda: self.canvas.create_line(50, 75, 65, 60, fill="black", width=2),
            # jambre droite
            lambda: self.canvas.create_line(80, 75, 65, 60, fill="black", width=2),
            # tête
            lambda: self.canvas.create_oval(60, 25, 70, 40, fill="black")
        ]

        self.body_parts_drawn = [False] * len(self.body_parts)

        self.letter_entry = tk.Entry(self.root)
        self.letter_entry.pack()

        self.incorrect_label = tk.Label(self.root, text="Incorrect letters:")
        self.incorrect_label.pack()

        self.correct_label = tk.Label(self.root, text="Correct letters:")
        self.correct_label.pack()

        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.result_label.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.play_hangman)
        self.submit_button.pack()
        self.submit_button.config(state="disabled")  # Désactivez le bouton "Submit" au départ

        # Listes pour les lettres correctes et incorrectes
        self.correct_letters = []
        self.incorrect_letters = []

        # Appelez initialize_game après un certain délai
        self.root.after(1000, self.initialize_game)

    def update_drawing(self):
        if self.attempts > 0 and self.attempts <= len(self.body_parts) and not self.body_parts_drawn[self.attempts - 1]:
            self.body_parts[self.attempts - 1]()
            self.body_parts_drawn[self.attempts - 1] = True

    def update_incorrect_letters(self):
        # Mettez à jour le label des lettres incorrectes
        self.incorrect_label.config(text="Incorrect letters: " + ", ".join(self.incorrect_letters))

    def update_correct_letters(self):
        # Mettez à jour le label des lettres correctes
        self.correct_label.config(text="Correct letters: " + ", ".join(self.correct_letters))

    def update_word_display(self):
        # Mettez à jour l'affichage du mot masqué
        self.word_label.config(text=self.show_word)

    def update_game(self):
        if self.game_started:
            guess_letter = self.letter_entry.get().lower()

            found = False

            if guess_letter.isalpha() and len(guess_letter) == 1:
                if guess_letter not in self.show_word:
                    if guess_letter not in self.incorrect_letters:
                        self.incorrect_letters.append(guess_letter)
                        self.update_incorrect_letters()

                updated_show_word = ""
                for i in range(len(self.word)):
                    if guess_letter == self.word[i]:
                        updated_show_word += guess_letter
                        found = True
                        if guess_letter not in self.correct_letters:
                            self.correct_letters.append(guess_letter)
                            self.update_correct_letters()
                    else:
                        updated_show_word += self.show_word[i]
                self.show_word = updated_show_word
                self.update_word_display()

                print(self.show_word)

                if "_" not in self.show_word:
                    self.result_label.config(text="Bravo!")  # Affiche "Bravo" lorsque le mot est complet
                    self.submit_button.config(state="disabled")  # Désactive le bouton "Submit"
                    print("Congratulations, you guessed the word!")

                if not found:
                    self.attempts += 1
                    self.update_drawing()  # Mettez à jour le dessin uniquement en cas de mauvaise lettre

    def initialize_game(self):
        with open("mots.txt", "r") as file:
            lines = file.readlines()

        rand_line = random.choice(lines)
        words = rand_line.strip().split()
        rand_word = random.choice(words)

        self.word = rand_word.lower()
        self.show_word = "_" * len(self.word)
        self.letter_entry.delete(0, tk.END)
        self.update_word_display()

        self.game_started = True  # Marquez que le jeu a commencé
        self.submit_button.config(state="normal")  # Activez le bouton "Submit" lorsque le jeu commence
        self.update_game()  # Mettez à jour le jeu dès le début

    def play_hangman(self):
        if not self.game_started:
            self.initialize_game()
        else:
            self.update_game()  # Mettez à jour le jeu

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
