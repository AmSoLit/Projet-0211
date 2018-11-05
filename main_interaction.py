from LogGenerator import *

from Data import *

import magic

import sys


print("""N'oubliez pas de doubler les antislash dans le chemin du fichier. \n""")
        
path = input ("Quel est le chemin du fichier à analyser ?\n ")
    
wantlog = input("Désirez-vous l'enregistrement des informations dans un fichier log.txt disponible sur votre bureau ?(o/n) \n")

bool = True

#Création du dataframe à partir du csv situé au niveau du chemin path

df = Data(path) 


#Enregistrement de l'appel de la fonction encoding qui renvoie l'encodage du document

bool = input("Afficher l'encodage ? (o/n) ")

encoding = df.encoding()

if (bool.lower() == "o") :

    encoding = df.encoding()
    print(encoding + "\n")

else :
    
    pass


#Enregistrement de l'appel de la fonction size_ko qui renvoie la taille du  fichier en kilo octects

bool = input("Afficher la taille du fichier ? (o/n) ")

size = df.size_ko()

if (bool.lower() == "o") :

    
    print(size + "\n")

else :
    
    pass

#Enregistrement de l'appel de la fonction date_last_modif qui renvoie la derniène date de modification du fichier

bool = input("Afficher la dernière date de modification ? (o/n) ")

last_modif = df.date_last_modif()

if (bool.lower() == "o") :

    
    print(last_modif + "\n")

else :
    
    pass


#Affichage du nombre de variables et d'observations

bool = input("Afficher le nombre de variables et d'observations ? (o/n) ")


if (bool.lower() == "o") :

    print("Ce fichier présente " +  str(df.nb_variables()) + " variables et comptabilise " + str(df.nb_observations()) + " observations")
    print("\n")

else :
    
    pass

#Affichage des informations concernant la table: nombre de variables qualitatives, nombre de variables quantitaives et les noms de ces variables.

bool = input("Afficher le nombre de variables qualitatives, le nombre de variables quantitaves et les noms de ces variables ? (o/n) ")

type_vari=""

if (bool.lower() == "o") :
    
    type_vari=df.type_var()
    print("\n")

else:
    
    pass



#Affichage des modalités de la variable qualitative

bool = input("Afficher les modalités de la variables qualitatives ? (o/n) ")


if (bool.lower() == "o") :
    
    print(df.nb_valeurs())
    print("\n")

else :
    
    pass

#Affichage de la fréquence
bool = input("Afficher les fréquences ? (o/n) ")

str1=df.freq_valeurs()

if (bool.lower() == "o") :
    
    print(str1)
    print("\n")

else :
    
    pass


#Affichage du minimum, du maximum, de la moyenne, de la médiane et de l'écart type de chaque variable quantitative

bool = input("Afficher les maximums, minimums, médianes, moyennes et écart-type ? (o/n) ")

max_min_etc = ""

if (bool.lower() == "o") :
    
    max_min_etc = df.max_min_etc()
    print("\n")

else :
    
    pass


#Retourne histogramme

bool = input("Enregistrer un histogramme ? (o/n) ")

if (bool.lower() == "o") :
    
    df.hist_figure_quantitative()
    print("Histogramme enregistré  à côté du script principal sous le nom de \"plot.pdf\" \n")

else :
    
    pass    

#Si l'utilisateur a dit oui à la proposition de création d'un log
if ((wantlog == 'o') | (wantlog =='O')):
    

                
   logpath = os.path.expanduser('~') + "\\Desktop"
   log = LogGenerator(logpath)
   log.ecriture(encoding+"\n")
   log.ecriture(size+"\n")
   log.ecriture("Ce fichier présente " +  str(df.nb_variables()) + " variables et comptabilise " + str(df.nb_observations()) + " observations \n")
   log.ecriture(str(type_vari)+"\n")
   log.ecriture(df.nb_valeurs())
   log.ecriture(str1+"\n")
   log.ecriture(str(max_min_etc))
    
elif ((wantlog == 'n') | (wantlog == 'N')) :

    print ("Aurevoir")

else :
    print ("Je n'ai pas compri!")

    

    


