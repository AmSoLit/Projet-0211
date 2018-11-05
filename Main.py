from LogGenerator import *

from Data import *

    
print("Bonjour ! \n")

interactivite = input("Souhaitez-vous utiliser la version intéractive ? o/n")

if ((interactivite == 'o') | (interactivite =='O')):

    import main_interaction

elif ((interactivite == 'n') | (interactivite == 'N')) :
     
    import main_classique

else :
    print("Erreur ! ")
