import os
import chardet
import time
import pandas
import matplotlib.pyplot as plt


#Trouver la taille du fichier en Kilo-octets 
def size_ko (path) :
    file_size_ko=os.path.getsize(path)/1024 #concersion octets / Koctets
    string_file_size_ko = str(file_size_ko)
    print(string_file_size_ko + "Ko")


#Trouver l'encodage d'un fichier
def encoding (path):
    file = open(path, 'rb').read()
    result = chardet.detect(file)
    print("Encoding: " + result['encoding'] )
    
#Dernière date de modification du fichier
def date_last_modif (path):
    print (time.ctime(os.path.getctime(path)))

#Chargement des données
def chargement(path) :
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 1, engine = 'python')
    except (e) :
        print(e)
    return dataframe, dataframe.shape

#Ecriture du premier CSV dans un autre avec un autre format
def reloading_csv(path):
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', engine ='python')
        dataframe.to_csv(path)
        print("Copie terminée")
    except (e):
        print(e)

#Retourner le nombre de colonnes et de lignes
def rows_columns (path) :
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 1, engine = 'python')
        lignes, colonnes = dataframe.shape
        print ("Il y a " + str(colonnes) + " colonnes et il a " + str(lignes) + " lignes")
    except (e) :
        print(e)

#Retourne le max, min, avg de sepal_length
def info_sepal_length (path):
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 0, engine = 'python')
        max_sepal_length = dataframe['Sepal.Length'].max()
        min_sepal_length = dataframe['Sepal.Length'].min()
        avg_sepal_length = dataframe['Sepal.Length'].mean()
        print('Max Sepal.Length ' + str(max_sepal_length))
        print('Min Sepal.Length ' + str(min_sepal_length))
        print('Average Sepal.Length ' + str(avg_sepal_length))

        
    except (e) :
        print(e)

#retourne le nombre de colonne
def nombre_colonnes (path):
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 0, engine = 'python', header = 0 )
    except (e) :
        print(e)
    print("Il y a "+str(len(dataframe.select_dtypes(include=['float64']).columns))+" variables qualitatives : " + str((dataframe.select_dtypes(include=['float64']).columns)) )
    print("Il y a "+str(len(dataframe.select_dtypes(exclude=['float64']).columns))+" variables quantitatives : " + str((dataframe.select_dtypes(exclude=['float64']).columns)) )
    #+len(dataframe.select_dtypes(include=['str']).columns))
    #print("Il y a "+str(len(dataframe.select_dtypes(exclude=['str']).columns))+" variables quantitatives")
    #return "Il y a "+ str(len(dataframe.columns))+" variables et il y a " +str(len(dataframe.columns)*len(dataframe.index)) + " valeurs"
    #return dataframe.dtypes
    print("Voici les max : " + str(dataframe.max()))
    print("Voici les min : " + str(dataframe.min()))
    print("Voici les moyennes : " + str(dataframe.mean()))
    print("Voici les médianes : " + str(dataframe.med()))

#Retourne un histogramme variables quantitatives
def hist_figure_quantitative (path) :
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 0, engine = 'python', header = 0 )
    except (e) :
        print(e)
    hist = dataframe.hist()
    plt.savefig(path+'figure.pdf')

#Retourne la fréquence
def hist_figure_qual (path) :
    try:
        dataframe = pandas.read_csv(path, sep =',|","', quotechar='"', index_col = 0, engine = 'python', header = 0 )
    except (e) :
        print(e)
    counts = dataframe.count()
    return counts

