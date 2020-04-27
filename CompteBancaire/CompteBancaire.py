class CompteBancaire:
    def __init__(self, nom="Dupond", solde=1000):
        self.nom = nom
        self.solde = solde
    def depot(self, somme):
        self.solde = self.solde + somme
    def retrait(self, somme):
        if(somme > self.solde):
            print("Solde insuffisant")
        else:
            self.solde = self.solde - somme
    def affiche(self):
        nom = self.nom
        solde = self.solde
        text = "Le solde du compte bancaire de {} est de {}€"
        print(text.format(nom, solde))

compte1 = CompteBancaire("Duchmol", 1000)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche() 