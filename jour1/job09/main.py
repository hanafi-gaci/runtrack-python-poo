class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Rasoir", 15.99, 5)
produit2 = Produit("Ordinateur", 799.99, 20)
produit3 = Produit("Télévision", 399.99, 10)


print("Informations initiales des produits :")
produit1.afficher()
produit2.afficher()
produit3.afficher()
print()


produit1.modifierNom("Shaver")
produit1.modifierPrixHT(12.99)

produit2.modifierNom("Macbook")
produit2.modifierPrixHT(899.99)

produit3.modifierNom("Ecran plat")
produit3.modifierPrixHT(349.99)

print("Informations mises à jour des produits :")
produit1.afficher()
produit2.afficher()
produit3.afficher()
print()
