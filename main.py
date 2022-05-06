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
        


class Cristal (Carte) :
    def __init__(self,mana,nom,description,valeur):
        Carte.__init__(self,mana,nom,description)
        self.__valeur = valeur
        self.type = "Cristal"
    
    def getValeur (self) : 
        return self.__valeur

    def getType (self):
        return self.type

    def cStats (self) : 
        print ("Cette carte est de type " + str(self.getType()) + ", coûte " + str(self.getMana()) + ", sa description est : " + str(self.getDes()) + " et sa valeur est de " + str(self.getValeur()))



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
troll = Creature(4,"Troll", "urqhrsghtightdi",10,5)
cristal1 = Cristal(2,"Petit cristal","",1)
cristal2 = Cristal(3,"Cristal moyen","",2)
cristal3 = Cristal(5,"Gros cristal","",3)
bdf = Blast(3,"Boule de feu", "ça brûle", 4)

#variables
activeplayer = player1
passiveplayer = player2

#fonctions
def jouer () : 
        choix = input("Entrez le numéro de la carte que vous voulez jouer. \n")
        if activeplayer.__main[choix].getType()!="Blast":
            prix = activeplayer.__main[choix].getMana()
            if prix<=activeplayer.getMMana(): 
                carte = activeplayer.__main.pop(choix)
                activeplayer.__zdj.append(carte)
                activeplayer.setMana(-prix)
                if choix.isCristal == True : 
                    activeplayer.setManaTot(carte.getValeur())
        else : 
            cible = (input("Entrez le numéro de votre cible (0 pour le joueur ennemi)"))
            if cible==0 : 
                passiveplayer.setMPV(-activeplayer.__main[choix].getValeur())
            else : 
                passiveplayer.__zdj[cible-1].setPV(-activeplayer.__main[choix].getValeur())
                if passiveplayer.__zdj[cible-1].getPV()<=0 : 
                    passiveplayer.__zdj.pop(cible-1)
                else : 
                    print(str(passiveplayer.__zdj[cible-1].getNom) + " a " + str(passiveplayer.__zdj[cible-1].getPV) + " pv.")

def attaquer():
    attaquant = activeplayer.__zdj[input("Avec quelle créature attaquez-vous ?")] 
    if attaquant.getType():
        cible = (input("Entrez le numéro de votre cible (0 pour le joueur ennemi)"))
        if cible==0 : 
            passiveplayer.setMPV(-activeplayer.__main[attaquant].getAtt())
        else : 
            passiveplayer.__zdj[cible-1].setPV(-activeplayer.__main[attaquant].getAtt())
            if passiveplayer.__zdj[cible-1].getPV()<=0 : 
                passiveplayer.__zdj.pop(cible-1)
            else : 
                print(str(passiveplayer.__zdj[cible-1].getNom) + " a " + str(passiveplayer.__zdj[cible-1].getPV) + " pv.")

def tour ():
    global activeplayer,passiveplayer
    player1.stats()
    player2.stats()
    choix = input("Jouer une carte, attaquer ou passer votre tour ?")
    if choix==1 : 
        jouer()
    elif choix==2 : 
        attaquer()
    else : 
        stock = activeplayer
        activeplayer = passiveplayer
        passiveplayer = stock
        


#code
player1.stats()
player2.stats()
troll.cStats()
cristal1.cStats()
bdf.cStats()

while player1.getMPV>=0 or player2.getMPV>=0 : 
    tour()


