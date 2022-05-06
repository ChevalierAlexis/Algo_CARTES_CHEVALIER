#Implémentation des classes

class Carte : 
    def __init__ (self,mana,nom,description):
        self.__mana = mana
        self.__nom = nom
        self.__des = description
        self.type = None

    def getMana (self):
        return self.__mana

    def getNom (self):
        return self.__nom

    def getDes (self):
        return self.__des

    def getType (self):
        return self.type

    def cStats (self) : 
        print ("Cette carte est de type " + str(self.getType()) + ", coûte " + str(self.getMana()) + ", sa description est : " + str(self.getDes()))





class Mage : 
    def __init__ (self,mNom):
        self.__mNom = mNom
        self.__mPv = 20
        self.__mManaTot = 10
        self.__mMana = 10
        self.__main = []
        self.__defausse = []
        self.__zdj = []
        self.type = "Mage"

    def getType (self):
        return self.type

    def getMnom (self):
        return self.__mNom

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

    def getMPV (self) : 
        return self.__mPv

    def setMPV (self, valeur):
        self.__mPv=self.__mPv+valeur    

    def stats (self):
        print(str(self.getMnom()) + " a " + str(self.getMPV()) + " pv et " + str(self.getMMana()) + "/" + str(self.getMManaTot()) + " mana")  

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
    def __init__(self,mana,nom,description,valeur):
        Carte.__init__(self,mana,nom,description)
        self.__valeur = valeur
        self.type = "Cristal"
    
    def getValeur (self) : 
        return self.__valeur

    def getType (self):
        return self.type



class Creature (Carte) : 
    def __init__(self,mana,nom,description,pv,att) : 
        Carte.__init__(self,mana,nom,description)
        self.__pv = pv
        self.__att = att
        self.type = "Creature"

    def getPV (self) : 
        return self.__pv

    def setPV (self, valeur) : 
        self.__pv = self.__pv+valeur

    def getAtt (self) : 
        return self.__att

    def getType (self):
        return self.type

    def getAtt (self):
        return self.__att

    def getPV (self):
        return self.__pv

    def cStats (self) : 
        print ("Cette carte est de type " + str(self.getType()) + ", coûte " + str(self.getMana()) + ", ses pv sont de " + str(self.getPV()) + ", son attaque est de " + str(self.getAtt()) +" et sa description est : " + str(self.getDes()))


 
class Blast (Carte) :
    def __init__ (self,mana,nom,description, valeurB) : 
        Carte.__init__(self,mana,nom,description)
        self.__valeurB = valeurB
        self.type = "Blast"

    def getValeurB (self) : 
        return self.__valeurB

    def getType (self):
        return self.type



#Création des objets
player1 = Mage(input ("Choisissez votre nom \n"))
player2 = Mage(input ("Choisissez votre nom \n"))
test = Creature(3,"Troll", "urqhrsghtightdi",10,5)

# cristal1 = Cristal(1)
# cristal2 = Cristal(2)
# cristal3 = Cristal(3)

#variables
activeplayer = player1
passiveplayer = player2

#code
player1.stats()
player2.stats()
test.cStats()

