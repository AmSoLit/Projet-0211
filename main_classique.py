from LogGenerator import *

from Data import *

import magic


print("""N'oubliez pas de doubler les antislash dans le chemin du fichier. \n""")
        
path = input ("Quel est le chemin du fichier à analyser ?\n ")
    
wantlog = input("Désirez-vous l'enregistrement des informations dans un fichier log.txt disponible sur votre bureau ?(o/n) \n")

#Création du dataframe à partir du csv situé au niveau du chemin path

df = Data(path)

#Enregistrement de l'appel de la fonction encoding qui renvoie l'encodage du document

encoding = df.encoding()

#Enregistrement de l'appel de la fonction size_ko qui renvoie la taille du  fichier en kilo octects

size = df.size_ko()

#Enregistrement de l'appel de la fonction date_last_modif qui renvoie la derniène date de modification du fichier

last_modif = df.date_last_modif()

#Affichage de l'encodage

print(encoding + "\n")

#Affichage de la taille du fichier

print(size + "\n")

#Affichage de la date de la dernière modification du fichier

print(last_modif + "\n")

#Affichage du nombre de variables et d'observations

print("Ce fichier présente " +  str(df.nb_variables()) + " variables et comptabilise " + str(df.nb_observations()) + " observations")
print("\n")

#Affichage des informations concernant la table: nombre de variables qualitatives, nombre de variables quantitaives et les noms de ces variables.

type_vari=df.type_var()
print("\n")

#Affichage du minimum, du maximum, de la moyenne, de la médiane et de l'écart type de chaque variable quantitative

max_min_etc = df.max_min_etc()
print("\n")

#Affichage des modalités de la variables qualitatives
print(df.nb_valeurs())
print("\n")

#Affichage de la fréquence
str1 = df.freq_valeurs()
print(str1)
print("\n")

#Retourne histogramme


df.hist_figure_quantitative()
print("Histogramme enregistré à côté du script principal sous le nom de \"plot.pdf\" \n")

    

#Si l'utilisateur a dit oui à la proposition de création d'un log
if (wantlog.lower() == 'o'):
    
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

    

    


