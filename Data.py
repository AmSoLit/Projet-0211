import pandas
import os
import chardet
import time
import re
import numpy
import matplotlib.pyplot as plt

class Data:

#Constructeur : créer un dataframe à partir du .csv situé à 'path'
    
    def __init__(self, path):
        self.chemin = path
        self.quant = []
        self.qual = []
        self.str3 = ""
        self.freq = []
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

#Affiche le nombre d'observations
    
    def nb_observations (self) :
        #print(self.dataframe.shape[0])
        return self.dataframe.shape[0]

#Affiche le nombre de variable
    
    def nb_variables(self):
        #print(self.dataframe.shape[1])
        return self.dataframe.shape[1]

#retourne le nombre et le type des variables
    
    def type_var(self) : 
        try : 
            for i in range(self.dataframe.shape[1]) : 
                if isinstance((self.dataframe.iloc[1, i]), numpy.number) : 
                    self.quant.append(self.dataframe.columns[i])
                else : 
                    self.qual.append(self.dataframe.columns[i])
            str1 = ''.join(str(f) for f in self.quant)
            str2 = ''.join(str(g) for g in self.qual)
            print("Il y a "+ str(len(self.qual))+ " variables qualitatives et "+ str(len(self.quant))+ " variables quantitatives.\nLes variables qualitatives sont : "+ str2 + " et les quantitatives sont : "+ str1 + " \n")
            return "Il y a "+ str(len(self.qual))+ " variables qualitatives et "+ str(len(self.quant))+ " variables quantitatives.\nLes variables qualitatives sont : "+ str2 + " et les quantitatives sont :  "+ str1 +"\n"

        except e :
            print(e)
        

#affiche le max des variables quantitatives
            
    def max_min_etc (self):
        pandas.set_option('display.max_columns', 7)
        quanti = self.dataframe.select_dtypes(include=['float64','int64']).describe().loc[['min','max','mean','50%','std']]
        print(quanti)
        return quanti


#Affiche le nombre de valeurs prises par la variable 

    def nb_valeurs(self) : 
        try : 
            for varqual in self.qual :  
                counter = self.dataframe[varqual].nunique()
                modalite = self.dataframe[varqual].unique()
                print("La variable ", varqual, " possède ", counter, " valeurs possibles : ", modalite )
        except e :
            print(e)


#retourne les fréquences
        
    def freq_valeurs(self) :
        try : 
            for columns in self.qual :  
                for i in range(0,len(self.qual)) :
                    counter = self.dataframe[columns].nunique()
                    for j in range (0,counter):
                        eff = self.dataframe[columns].value_counts()
                        self.freq.append(str(eff.keys()[j])+"  "+str(eff.values[j]))
                    str1 = ''.join(str(f) for f in self.freq)
                    return "Fréquences : \n"+ str1
                        
        except e :
            print(e)
        

#Retourne un histogramme variables quantitatives
                
    def hist_figure_quantitative(self):     
        quanti = self.dataframe.select_dtypes(include=['float64','int64']).describe().loc[['min','max','mean','50%','std']]
        #"Sauvegarde du plot de distribution"
        quanti.plot.bar()
        plt.savefig("plot.pdf")
                
        
