import os
import chardet
import time

#Trouver la taille du fichier en Kilo-octets 
def size_ko (path) :
    file_size_ko=os.path.getsize(path)/1024 #concersion octets / Koctets
    string_file_size_ko = str(file_size_ko)
    print(string_file_size_ko + "Ko")



#Trouver l'encodage d'un fichier
def encoding (path):
    file = open(path, 'rb').read()
    result = chardet.detect(file)
    print("Encoding: " + result['encoding'] + " Confidence " +  str(result['confidence']))
    
#Dernière date de modification du fichier
def date_last_modif (path):
    print (time.ctime(os.path.getctime(path)))


