from LogGenerator import *

from Data import *

def main ():
    
    print(""" Bonjour ! N'oubliez pas de doubler les antislash dans le chemin du fichier. \n""")
    
    path = input ("Quel est le chemin du fichier à analyser ?(o/n) \n ")
    
    wantlog = input("Désirez-vous l'enregistrement des informations dans un fichier log.txt disponible sur votre bureau ?")
    
    if ((wantlog == 'o') | (wantlog =='O')):
        
        logpath = os.path.expanduser('~') + "\\Desktop"
        
        log = LogGenerator(logpath)
        
    elif ((wantlog == 'n') | (wantlog == 'N')) :
        
        pass
    
    else :
        
        print("Je n'ai pas compris votre réponse !")
        
    usedData = Data(path)

    quest = input("Voulez-vous voir l'encodage, la taille et la date de la dernière modification du fichier ? (o/n) \n ")

    if ((quest == 'o') | (quest =='O')):

        encoding = usedData.encoding()

        size = usedData.size_ko()

        last_modif = usedData.date_last_modif()

        if ((wantlog == 'o') | (wantlog == 'O')) :

            log.ecriture(encoding)

            log.ecriture(size)

            log.ecriture(last_modif)

    nbr_qual = usedData.nombre_variables_qualitatives()

    liste_qual = usedData.nom_variables_qualitatives()

    print(nbr_qual + " : ")
    
    for i in range (1, len(liste_qual)) :
        
        print (usedData.net(liste_qual[i]) + "\n")

    nbr_quan = usedData.nombre_variables_quantitatives()

    liste_quan = usedData.nom_variables_quantitatives()

    print(nbr_quan + " : ")

    #plot etc...
    
    for i in range (1, len(liste_quan)) :
        
        print(usedData.net(liste_quan[i]) + "\n")

    for i in range (1, len(liste_quan)) :

        print(usedData.net(liste_quan[i]) + " : " + usedData.max(usedData.net(liste_quan[i])) )
    
