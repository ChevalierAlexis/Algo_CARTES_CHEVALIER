class Carte : 
    def __init__ (self,mana,nom,description):
        self.__mana = mana
        self.__nom = nom
        self.__des = description
        self.isCristal = False

    def getMana (self):
        return self.__mana

class Mage : 
    def __init__ (self,mNom):
        self.__mNom = mNom
        self.__mPv = 20
        self.__mManaTot = 10
        self.__mMana = 10
        self.__main = []
        self.__defausse = []
        self.__zdj = []

    def getMMana (self):
        return self.__mMana

    def setMana (self,valeur):
        self.__mMana=self.__mMana+valeur
        if self.__mMana>10 : 
            self.__mMana=10

    def getMManaTot (self):
        return self.__mManaTot

    def setManaTot (self,valeur):
        self.__mManaTot=self.__mManaTot+valeur

    def getPV (self) : 
        return self.__mPv

    def setPV (self, valeur):
        self.__mPv=self.__mPv+valeur      

    def jouer (self) : 
        choix = input("Entrez le numéro de la carte que vous voulez jouer. \n")
        prix = self.__main[choix].getMana()
        if prix<=self.getMMana(): 
            carte = self.__main.pop(choix)
            self.__zdj.append(carte)
            self.setMana(-prix)
            if choix.isCristal == True : 
                self.setManaTot(carte.getValeur())
        
class Cristal (Carte) :
    def __init__(self,valeur):
        self.__valeur = valeur
        self.isCristal = True
    
    def getValeur (self) : 
        return self.__valeur