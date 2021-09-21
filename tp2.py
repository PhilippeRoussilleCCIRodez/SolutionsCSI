"""Fichier du TP 2."""
from math import sin
from random import randint
import time

def age():
    """Exo 1"""
    age_str = input("Entrez votre âge :")
    try:
        print("Vous avez ", int(age_str), "ans.")
    except ValueError:
        print("Vous n'avez pas entré un nombre.")

def fonction(variable_x):
    """Exo 2."""
    try:
        variable_y = sin(variable_x)/variable_x
    except ZeroDivisionError:
        variable_y = 1
    return variable_y

def ouvrir():
    """Exo 3"""
    # Cette instruction désactive pylint pour la variable non utilisée
    # pylint: disable=W0612
    fichier_non_existant = True
    while fichier_non_existant:
        nom_fichier = input("Entrez un nom de fichier :")
        try:
            with open(nom_fichier,encoding="utf-8") as fichier:
                fichier_non_existant = False
        except FileNotFoundError:
            print("Ce fichier n'existe pas.")

def jeu_pas_trop_super():
    """Exo 4."""
    temps = randint (0 ,100)
    print(f"Vous devez arrêter le programme sur {temps}.")
    print("Pour arrêter le programme, il faut faire Ctrl+C.")
    print("Appuyer sur Entrée pour commencer...")
    _ = input()
    i = 0
    try:
        while i < 100 :
            i += 1
            print(i)
            time.sleep(0.2)
        print("Temps écoulé ! Perdu...")
    except KeyboardInterrupt:
        print()
        if i == temps:
            print("Bravo !")
        elif abs(i - temps) < 4: # contraction de else if
            print("Presque !")
        else:
            print("Raté !")

jeu_pas_trop_super()

# ####################################
# # Partie magie-vaudou
# # (sort du contexte du cours)
# import signal
# class TempsEcoule(Exception):
#     pass

# def gestion_alarme(s, f):
#     raise TempsEcoule()

# def lever_une_exception_au_bout_de(secondes):
#     signal.signal(signal.SIGALRM, gestion_alarme)
#     signal.alarm(secondes)
# ####################################
# def exo7():
#     """Demande à l'utilisateur de faire l'exercice 7."""
#     # Description un peu plus explicite :
#     # On enregistre un signal particulier, le signal "ALARM"
#     # qui permet de déclencher quelque chose après n secondes.
#     # Ici, on indique que si on reçoit le signal ALARM,
#     # on exécute la fonction gestion_alarme
#     # qui ne fait rien de plus que de lever l'exception TempsEcoule.
#     for i in range(10):
#         nombre1 = randint(0, 100)
#         nombre2 = randint(0, 100)
#         solution = nombre1 + nombre2
#         lever_une_exception_au_bout_de(2)
#         bonne_reponse = False
#         try:
#             print("Combien font",nombre1, " + ",nombre2,"? Vous avez dix secondes...")
#             solution_utilisateur = int(input(">"))
#             bonne_reponse = (solution == solution_utilisateur)
#         except TempsEcoule:
#             print("Boooouh ! Vous avez été trop lent...")
#             bonne_reponse = False
#         if bonne_reponse:
#             print("Bravo !")
#         else:
#             print("PERDU ! La bonne réponse évidente était ", solution, "!")

# exo7()
