from msilib.schema import Class


class Carte : 
    def __init__ (self,mana,nom,description):
        self.__mana =mana
        self.__nom = nom
        self.__des = description

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

    def getPV (self) : 
        return self.__mPv

    def setPV (self, valeur):
        self.__mPv=self.__mPv+valeur      

    # def jouer (self) : 
    #     choix = input("Entrez le numéro de la carte que vous voulez jouer. \n")
    #     if self.__main[choix]: 
    #         carte = self.__main.pop(choix)
    #         self.__zdj.append(carte)
        