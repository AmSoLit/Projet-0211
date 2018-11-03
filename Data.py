import pandas
import os
import chardet
import time
import re

class Data:

#Constructeur : créer un dataframe à partir du .csv situé à 'path'
    def __init__(self, path):
        self.chemin = path
        try:
            self.dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 0, engine = 'python', header = 0 )
            print('Le fichier ' + path + ' a été chargé')
        except () :
            print('Erreur de chargement du fichier. Veuillez entrer un chemin correct !')

#size_ko permet d'afficher la taille en Kilo-Octects du fichier situé à 'chemin'
    def size_ko (self) :
        file_size_ko=os.path.getsize(self.chemin)/1024 #concersion octets / Koctets
        string_file_size_ko = str(file_size_ko)
        return("Taille du fichier : " + string_file_size_ko + "Ko")

#Trouver l'encodage d'un fichier
    def encoding (self):
        file = open(self.chemin, 'rb').read()
        result = chardet.detect(file)
        return("Encoding : " + result['encoding'])

#Dernière date de modification du fichier
    def date_last_modif (self):
        return ("Dernière modification : " + str(time.ctime(os.path.getctime(self.chemin))))

#Affiche le nombre de valeurs d'observations
    def nombre_observation(self) :
        observations = self.dataframe.count()
        print(observations)

#affiche le type des valeurs de chaque colonne
    def display_columns_type(self):
        return self.dataframe.dtypes

#Compte le nombre de variables qualitatives

    def nombre_variables_qualitatives (self) :
        return "Il y a " + str(len(self.dataframe.select_dtypes(exclude=['float64']).columns))+ " variable(s) qualitative(s)"

#Compte le nombre de variables quantitatives
    def nombre_variables_quantitatives (self) :
        return "Il y a " + str(len(self.dataframe.select_dtypes(include=['float64']).columns))+ " variable(s) quantitative(s)"

#Affiche le nom des variables quantitatives
    def nom_variables_quantitatives(self):
        transition = str((self.dataframe.select_dtypes(include=['float64']).columns))
        regex = r'[A-Z][a-z]*["."]?[A-Z]?[a-z]*'
        tom = re.findall(regex,transition)
        return (tom)

#Nettoyeur de chaine
    def net (self,chaine) :
        return chaine.strip('"')


#Affiche le nom des variables qualtitatives
    def nom_variables_qualitatives(self):
        transition = str((self.dataframe.select_dtypes(exclude=['float64']).columns))
        regex = r'[A-Z][a-z]*["."]?[A-Z]?[a-z]*'
        tom = re.findall(regex,transition)
        return (tom)


#Affiche min 
    def min(self, variable) :
        minimum = dataframe[variable].min()
        return (minimum)

#Affiche max
    def max(self, variable) :
        maximum = self.dataframe[variable].max()
        return (maximum)

#Affiche la médiane
    def med(self, variable) :
        mediane = self.dataframe[variable].max()
        return (mediane)
    
#Affiche l'écart type
    def ecart_type(self, variable) :
        std = self.dataframe[variable].std()
        return (std)
    
    
