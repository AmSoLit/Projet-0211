class LogGenerator :
    def __init__(self, path) :
        self.chemin = path
        
        

    def ecriture(self, str):
        with open(self.chemin+"\\log.txt",'a',encoding = 'utf-8') as sortie :
                sortie.write(str+"\n")
