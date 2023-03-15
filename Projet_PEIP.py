"""
Enoncé:

Récursivité informatique 

On  s’intéresse  aux  constructions  récursives  dont  la  caractéristique  est  de  se  définir  par rapport à elles-mêmes. 
    - donner des exemples généraux de telles constructions En programmation informatique, la solution d’un problème est récursive si elle s’exprime à partir du même problème appliqué à des cas « plus simples ». 
    - à quoi sert le cas de base dans ce contexte ? 
    - donner un exemple simple de problème récursif, expliquer. 
    - étudier le problème récursif des tours de Hanoï, expliquer. La récursivité est une généralisation de la récurrence mathématique, expliquer en quoi ? Tout problème récursif peut se résoudre de manière itérative. 
    - qu’est-ce qu’une itération en programmation ? 
    - réécrire l’exemple simple du problème récursif que vous avez précédemment choisi avec une itération. 
    - quels sont les avantages et les inconvénients des deux approches ? 
Pour terminer ce travail, vous étudierez une application de la récursivité : 
    par exemple le backtracking (ou autre) pour lequel vous donnerez une définition et quelques exemples de problèmes de cette nature, vous décrirez l’utilisation de la récursivité dans ce contexte et vous  écrirez  en  pseudo-code  un  algorithme  récursif général  de  résolution  de  ce  type  de problème. 
    
NB : la recherche sur Internet est largement recommandée mais ce que vous écrirez dans votre rapport final devra être parfaitement compris.

"""

#!bin/bash/python3
from prettytable import PrettyTable as PT   #ajout du package pour le pretiffy du tableau
import csv                                  #ajout du package pour la sauvegarde en .csv
import os                                   #ajout de package non-necessaire
import time                                 #ajout de package non-necessaire

#Ajout d'une classe pour le menu

class color:
#   PURPLE = '\033[95m'
   CYAN = '\033[96m'
#   DARKCYAN = '\033[36m'
#   BLUE = '\033[94m'
#   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#Initialisation de la variable cpt car sinon Undefined variable 'cpt' dans la fonction recursive
cpt=0

#fonction recursive de résolution du probleme de la tour de hanoi
def hanoi(n,a=1,b=2,c=3):
    global cpt
    if (n > 0):
        hanoi(n-1,a,c,b)
        print( "Déplace l'anneau le plus au dessus de la tour ",a," sur la tour",c) 
        hanoi(n-1,b,a,c)
        cpt+=1

while True:
#Initialisation des variables necessaire a chaque entrée dans le programme /remise a zero
    cpt=0
    mvt=[]
    ano=[]

#Purge du terminal
    os.system("cls")

#Création d'un menu
#Ajout du titre
    print("                " + color.BOLD + color.UNDERLINE + color.CYAN + 'Projet d\'ingénierie PEIP \n' + color.END)
#Ajout des options
    print(color.BOLD + "   1) - Calculer les mouvements d'un seul jeu d'anneau \n   2) - Calculer toutes les itérations de 1 jusqu'au nombre d'anneau saisi dans l'input suivante \n   0) - Si vous souhaitez quittez le programme" + color.END)
#Ajout de l'input
    menu=int(input("Que souhaitez vous faire ? (Choisissez "+ color.UNDERLINE + color.BOLD + "1" + color.END +" ou "+ color.UNDERLINE + color.BOLD + "2" + color.END + " ou " + color.UNDERLINE + color.BOLD + "0"+ color.END+ ") : ") or "-1")

#Redirection en fonction des choix
#Choix 1 -> Seulement une résolution pour un nombre n d'anneaux
    if(menu == 1 ):
#Purge du terminal
        os.system("cls")
#Input pour le nombre d'anneau
        n=int(input("Nombre d'anneaux sur la premiere tour de Hanoï : "))
#Verification de la véracité de l'input
        if(n>0):
#Appel a la fonction hanoi
            hanoi(n)
#Nombre de mouvement effectuer
            print(cpt, "appels \n")
#Pause de la boucle en attente d'une interaction de l'utilisateur
            os.system("pause")
        else:
#Affichage de l'erreur en cas de non-veracité de l'input 
            print(color.BOLD + color.UNDERLINE + color.RED + "Le nombre maximum d'anneaux ne peut pas etre inferieur ou égale a 0")
            os.system("pause")

#Choix 2 -> Résolution pour un nombre de 1 a n d'anneaux
    elif(menu == 2):
        os.system("cls")
        max=int(input("Nombre maximum d'anneaux : "))
        #max=5   #utilisation du fixage de la valeur lors du deboggage
        if(max>0):
            for i in range(1,max+1):    #max est exclu, on rajoute donc +1 pour comprendre max dans l'intervalle
                print("Nombre d'anneau :", i,"\n")
                ano.append(i)           #
                hanoi(i)
                print(cpt, "appels \n")
                mvt.append(cpt)
                cpt=0
#Affichage dans le terminal des résultats
            myTable = PT(["Nombre d'anneaux", "Nombre de déplacements"])
            for x in range(len(ano)):
                myTable.add_row([ano[x], mvt[x]])
            print(myTable)
#Pour eviter les erreurs, on taskkill calc au cas ou le fichier est encore ouvert
#ATTENTION, NE PAS AVOIR UN AUTRE DOCUMENTS CALC SINON IL SERA FERME AUSSI
            try:
                os.system("taskkill /f /im soffice.bin /t")
                time.sleep(2)
            finally:
#Enregistrement au format .csv pour pouvoir ouvrir kes resultats sous excels
                with open('hanoi.csv', 'w+', encoding='latin1', newline='')as f:
                    fieldnames = ["Nombre d'anneaux", "Nombre de déplacements"]
                    w = csv.DictWriter(f, fieldnames=fieldnames)
                    w.writeheader()
                    for x in range(len(ano)):
                        w.writerow({"Nombre d'anneaux": ano[x], "Nombre de déplacements": mvt[x]})
#Demande de sortie du programme
                exit=input("Souhaitez vous quittez? (Y / N) ")
                if(exit=='Y'):
                    break
                else:
                    pass
#Affichage de l'erreur en cas de non-veracité de l'input 
        else:
            print(color.BOLD + color.UNDERLINE + color.RED + "Le nombre maximum d'anneaux ne peut pas etre inferieur ou égale a 0")
            os.system("pause")
#On passe par défaut -1 en parametre d'input, si un utilisateur ne saisi pas d'input, il est redirigé ici, -1 n'étant pas un 
    elif(menu == -1):
        print(color.BOLD + color.UNDERLINE + color.RED + "Veuillez entrer un chiffre")
        os.system("pause")
        os.system("cls")
#On quitte le programme si l'utilisateur saisi 0
    elif(menu == 0):
        print("          " + color.UNDERLINE + color.YELLOW + "Vous quittez le programme"+color.END)
        break
#Erreur si l'utilisateur rentre un chifre != de 1 ou 2 ou 0
    else:
        print(color.BOLD + color.UNDERLINE + color.RED + "Veuillez entrer soit 1 soit 2 soit 0 ")
        os.system("pause")
        os.system("cls")
