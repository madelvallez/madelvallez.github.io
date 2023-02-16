from Plateau import *

class Controleur:
    def __init__(self, dim_plateau = 4):
        self.plateau = Plateau(dim_plateau)
        self.fin_partie = False
        input(" Bienvenue dans le jeu 2048.")
        print("Pour  faire un mouvement, utilise les mots \"droite\", \"gauche\", haut\" et \"bas\" ")
        print("Pour mettre fin à la partie tapes \"fin\"")

    def tour(self):
        print(self.plateau)
        mouvement =input("Donne un mouvement : ")
        if mouvement == "droite": 
            self.plateau.mouvement_droite()
        elif mouvement == "gauche":
            self.plateau.mouvement_gauche()
        elif mouvement == "haut":
            self.plateau.mouvement_haut()
        elif mouvement == "bas" :
            self.plateau.mouvement_bas()
        elif mouvement == "fin" :
            self.fin()
        else :
            print("Ceci n'est pas un mouvement \n Tapes \"droite\", \"gauche\", haut\" ou \"bas\" pour jouer \n")
            print("Pour mettre fin à la partie tapes \"fin\"")
            self.tour()

    def fin(self):
        print("Est-tu sur(e) de vouloir mettre fin à la partie? Tu perdra ta progression ")
        rep = input("Réponds par \"oui\" ou \"non\" : ")
        if rep == "oui":
            self.fin_partie = True
        else :
            self.tour()