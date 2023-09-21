import tkinter as tk  # Importe la bibliothèque Tkinter pour créer l'interface utilisateur
import random  # Importe la bibliothèque random pour générer des mots aléatoires

class HangmanApp:
    def __init__(self, root):
        # Initialise la fenêtre Tkinter
        self.root = root  # 'self.root' est une référence à la fenêtre principale de l'application
        self.root.title("StickMan")  # Définit le titre de la fenêtre

        # Crée un canevas pour dessiner le pendu
        self.canvas = tk.Canvas(self.root, width=100, height=150)  # Crée un élément de canevas dans la fenêtre
        self.canvas.pack()  # Affiche le canevas dans la fenêtre

        # Initialise les variables du jeu
        self.attempts = 0  # Nombre d'essais
        self.max_attempts = 10  # Maximum d'essais autorisés
        self.show_word = ""  # Mot en cours de découverte
        self.word = ""  # Mot à deviner

        # Variable pour suivre si le jeu a commencé
        self.game_started = False

        # Liste des fonctions de dessin pour le pendu
        self.body_parts = [
            # Dessine la base du pendu
            lambda: self.canvas.create_line(20, 80, 60, 80, fill="black", width=4),
            # Dessine le poteau
            lambda: self.canvas.create_line(40, 20, 40, 80, fill="black", width=4),
            # Dessine la barre horizontale du haut
            lambda: self.canvas.create_line(20, 20, 80, 20, fill="black", width=4),
            # Dessine la diagonale
            lambda: self.canvas.create_line(40, 30, 60, 20, fill="black", width=4),
            # Dessine la corde
            lambda: self.canvas.create_line(65, 20, 65, 25, fill="black", width=2),
            # Dessine le torse
            lambda: self.canvas.create_line(65, 30, 65, 60, fill="black", width=2),
            # Dessine le bras
            lambda: self.canvas.create_line(50, 50, 80, 50, fill="black", width=2),
            # Dessine la jambe gauche
            lambda: self.canvas.create_line(50, 75, 65, 60, fill="black", width=2),
            # Dessine la jambe droite
            lambda: self.canvas.create_line(80, 75, 65, 60, fill="black", width=2),
            # Dessine la tête
            lambda: self.canvas.create_oval(60, 25, 70, 40, fill="black")
        ]

        # Liste pour suivre si chaque partie du pendu a été dessinée
        self.body_parts_drawn = [False] * len(self.body_parts)

        # Crée un champ de saisie pour deviner les lettres
        self.letter_entry = tk.Entry(self.root)  # Crée un champ de texte dans la fenêtre
        self.letter_entry.pack()  # Affiche le champ de texte dans la fenêtre

        # Étiquette pour afficher les lettres incorrectes
        self.incorrect_label = tk.Label(self.root, text="Incorrect letters:")  # Crée une étiquette de texte
        self.incorrect_label.pack()  # Affiche l'étiquette dans la fenêtre

        # Étiquette pour afficher les lettres correctes
        self.correct_label = tk.Label(self.root, text="Correct letters:")  # Crée une autre étiquette de texte
        self.correct_label.pack()  # Affiche l'étiquette dans la fenêtre

        # Étiquette pour afficher le mot masqué
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))  # Crée une étiquette de texte plus grande
        self.word_label.pack()  # Affiche l'étiquette dans la fenêtre

        # Étiquette pour afficher le résultat ("Bravo" ou autre)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 24))  # Crée une autre grande étiquette de texte
        self.result_label.pack()  # Affiche l'étiquette dans la fenêtre

        # Bouton pour soumettre une lettre
        self.submit_button = tk.Button(self.root, text="Submit", command=self.play_hangman)  # Crée un bouton
        self.submit_button.pack()  # Affiche le bouton dans la fenêtre
        self.submit_button.config(state="disabled")  # Désactivez le bouton "Submit" au départ

        # Listes pour les lettres correctes et incorrectes
        self.correct_letters = []  # Lettres correctes devinées
        self.incorrect_letters = []  # Lettres incorrectes devinées

        # Appelez initialize_game après un certain délai
        self.root.after(1000, self.initialize_game)  # Programme un appel à la fonction initialize_game après 1000 millisecondes

    def update_game(self):
        # Met à jour l'état du jeu en fonction de la lettre soumise par le joueur

        if self.game_started:
            guess_letter = self.letter_entry.get().lower()  # Obtient la lettre soumise par le joueur

            found = False  # Variable pour indiquer si la lettre soumise est dans le mot

            if guess_letter.isalpha() and len(guess_letter) == 1:
                # Vérifie si la lettre soumise est alphabétique et une seule lettre

                if guess_letter not in self.show_word:
                    # Si la lettre n'est pas déjà dans le mot en cours de découverte
                    if guess_letter not in self.incorrect_letters:
                        self.incorrect_letters.append(guess_letter)  # Ajoute la lettre incorrecte
                        self.update_incorrect_letters()  # Met à jour l'étiquette des lettres incorrectes

                updated_show_word = ""  # Initialise une variable pour stocker la mise à jour du mot en cours de découverte
                for i in range(len(self.word)):
                    # Parcourt chaque lettre du mot à deviner
                    if guess_letter == self.word[i]:
                        # Si la lettre soumise par le joueur correspond à la lettre du mot actuelle
                        updated_show_word += guess_letter  # Ajoute la lettre correcte à la mise à jour du mot
                        found = True  # Marque que la lettre soumise a été trouvée dans le mot
                        if guess_letter not in self.correct_letters:
                            self.correct_letters.append(guess_letter)  # Ajoute la lettre correcte à la liste des lettres correctes
                            self.update_correct_letters()  # Met à jour l'étiquette des lettres correctes
                    else:
                        updated_show_word += self.show_word[i]  # Sinon, ajoute la lettre du mot en cours de découverte
                self.show_word = updated_show_word  # Met à jour le mot en cours de découverte avec les nouvelles lettres correctes
                self.update_word_display()  # Met à jour l'affichage du mot masqué

                if "_" not in self.show_word:
                    # Si le mot masqué ne contient plus de tirets bas, le joueur a gagné
                    self.result_label.config(text="Bravo!")  # Affiche "Bravo" sous le dessin
                    self.submit_button.config(state="disabled")  # Désactive le bouton "Submit"

                if not found:
                    self.attempts += 1
                    self.update_drawing()  # Met à jour le dessin du pendu en cas de mauvaise lettre

    def initialize_game(self):
        # Initialise une nouvelle partie du jeu

        with open("mots.txt", "r") as file:
            lines = file.readlines()

        rand_line = random.choice(lines)  # Choisis une ligne au hasard dans le fichier de mots
        words = rand_line.strip().split()  # Divise la ligne en mots
        rand_word = random.choice(words)  # Choisis un mot au hasard parmi les mots de la ligne

        self.word = rand_word.lower()  # Convertit le mot en minuscules
        self.show_word = "_" * len(self.word)  # Initialise le mot en cours de découverte avec des tirets bas
        self.letter_entry.delete(0, tk.END)  # Efface le champ de saisie
        self.update_word_display()  # Met à jour l'affichage du mot masqué

        self.game_started = True  # Marque que le jeu a commencé
        self.submit_button.config(state="normal")  # Active le bouton "Submit"
        self.update_game()  # Met à jour le jeu dès le début

    def play_hangman(self):
        # Fonction appelée lorsque le joueur appuie sur le bouton "Submit"

        if not self.game_started:
            # Si le jeu n'a pas encore commencé, initialise une nouvelle partie
            self.initialize_game()
        else:
            # Sinon, met à jour le jeu avec la lettre soumise par le joueur
            self.update_game()

    def update_drawing(self):
        # Met à jour le dessin du pendu en fonction du nombre d'essais infructueux

        if self.attempts > 0 and self.attempts <= len(self.body_parts) and not self.body_parts_drawn[self.attempts - 1]:
            self.body_parts[self.attempts - 1]()  # Appelle la fonction de dessin correspondante
            self.body_parts_drawn[self.attempts - 1] = True  # Marque la partie du pendu comme dessinée

    def update_incorrect_letters(self):
        # Met à jour l'étiquette des lettres incorrectes
        self.incorrect_label.config(text="Incorrect letters: " + ", ".join(self.incorrect_letters))

    def update_correct_letters(self):
        # Met à jour l'étiquette des lettres correctes
        self.correct_label.config(text="Correct letters: " + ", ".join(self.correct_letters))

    def update_word_display(self):
        # Met à jour l'affichage du mot masqué
        self.word_label.config(text=self.show_word)

if __name__ == "__main__":
    root = tk.Tk()  # Crée une instance de fenêtre Tkinter
    app = HangmanApp(root)  # Crée une instance de l'application HangmanApp
    root.mainloop()  # Lance la boucle principale de l'interface utilisateur Tkinter


# self est utilisé pour faire référence à des attributs et méthodes de l'instance de la classe HangmanApp.
# Cela permet d'accéder aux variables et fonctions spécifiques à chaque instance de la classe,
# ce qui est essentiel pour créer des applications orientées objet.

# Une classe (HangmanApp) a été utilisée pour encapsuler les données et le comportement du jeu dans un objet unique.
# Cela permet de structurer le code de manière plus organisée et de gérer facilement les interactions entre différentes parties du jeu.

# La classe HangmanApp est instanciée avec app = HangmanApp(root),
# où root est la fenêtre principale de l'application Tkinter. 
# L'objet app représente ensuite l'ensemble du jeu Hangman et permet d'appeler ses méthodes pour gérer le jeu.

# Les méthodes de la classe (__init__, update_game, initialize_game, etc.) sont des fonctions spécifiques à l'objet app 
# et utilisent self pour accéder aux attributs de l'instance (par exemple, self.canvas, self.word, self.submit_button, etc.) 
# et effectuer des opérations spécifiques au jeu.