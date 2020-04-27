class DateNaissance:
    def __init__(self, jour, mois, anne):
        self.jour = jour
        self.mois = mois
        self.anne = anne
    def ToString(self):
        txt = "{}/{}/{}"
        return txt.format(self.jour, self.mois, self.anne)

class Personne:
    def __init__(self, nom, prenom, date):
        self.nom = nom
        self.prenom = prenom
        self.date = date
    def Affichage(self):
        txtNom = "Nom: {}"
        print(txtNom.format(self.nom))
        txtPrenom = "Prénom: {}"
        print(txtPrenom.format(self.prenom))
        txtDate = "Date de naissance: {}"
        print(txtDate.format(self.date))

class Employe(Personne):
    def __init__(self, nom, prenom, date, salaire):
        self.salaire = salaire
        self.nom = nom
        self.prenom = prenom
        self.date = date
    def Affichage(self):
        txt = "Nom: {}\nPrénom: {}\nDate de naissance: {}\nSalairee: {}"
        print(txt.format(self.nom, self.prenom, self.date, self.salaire))

class Chef(Employe):
    def __init__(self, nom, prenom, date, salaire, service):
        self.salaire = salaire
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.service = service
    def Affichage(self):
            Employe.Affichage(self)
            txt = "Service: {}"
            print(txt.format(self.service))

date = DateNaissance(20,12,1997)


a = Personne("Lilian1", "Séon", date.ToString())
a.Affichage()
print("_____________________")


b = Employe("Lilian2", "Séon", date.ToString(), 12000)
b.Affichage()
print("_____________________")


c = Chef("Lilian3", "Séon", date.ToString(), 56000, "Resource Humaine")
c.Affichage()