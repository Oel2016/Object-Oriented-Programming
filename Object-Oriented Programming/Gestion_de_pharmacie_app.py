class client :                         #génère un client
    def __init__(self,nom,credit):
        self.nom = nom
        self.credit = credit
    def __str__(self):                 #affiche les attributs d'un client
        return 'Client:{} , credit:{}'.format(self.nom,self.credit)

class medicament :                     #génère un médicament
    def __init__(self,nom,prix,stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock
    def __str__(self):                 #affiche les attributs d'un médicament
        return 'Médicament:{} , stock:{}'.format(self.nom,self.stock)

class pharmacie :                      # génère une pharmacie dont on souhaite gérer, elle prend comme paramètre une liste de clients et une liste de médicaments de la pharmacie
    def __init__(self,listeclients,listemedicaments):
        self.listeclients = listeclients              # liste de clients
        self.listemedicaments = listemedicaments      #liste de médicament

    @property
    def affichage(self):                              # afficahge des clients et des médicament de la pharmacie
        print("____affichage des  clients_____")
        print("********************************")
        for clt in self.listeclients :
            print(clt)
        print("********************************")
        print("____affichage des médicaments_____")
        print("************************************")
        for med in self.listemedicaments :
            print(med)
        print("********************************")
    @property
    def approvisionnement(self):
        medicament = self.liremedicament              #vérifie si le médicament se trouve dans la pharmacie , si c'est le cas il le stocke dans la variable mediacment
        qte = int(input('Entrez la quantité à approvisionner: '))
        medicament.stock += qte                       # incrémentation de la quantité du médicament à approvisionner
    @property
    def liremedicament(self):                         # vérifie si le médicament se trouve dans la pharmacie , si c'est le cas , il retourne l'objet médicament une fois on saisit un nom valide.
        medicament = input('Entrez le nom du médicament: ')
        while True :
            for med in self.listemedicaments :
                if med.nom == medicament :
                    return med
            medicament = input('Médicament invalide,\n enregistrez le médicament \n ou entrez un nom du médicament valide: ')
    @property
    def lireclient(self):                            # même travail realisé par liremedicament sauf cette fois on le fait pour les clients
        client = input('Entrez le nom du client: ')
        while True :
            for clt in self.listeclients :
                if clt.nom == client :
                    return clt
            client = input('Client invalide,\n enregistez le client \n ou entrez un nom valide: ')
    @property
    def enregistrement(self):                        # enregistre un médicament
        nom = input('Entrez le nom du medicament: ')
        prix = int(input('Entrez le prix: '))
        stock = int(input('Entrez la quantité du stock: '))
        med= medicament(nom,prix,stock)
        self.listemedicaments.append(med)
    @property
    def enregistrement_client(self):                 #enregistre un client
        nom = input('Entrez le nom du client: ')
        credit = int(input('Entrez le crédit: '))
        clt= client(nom,credit)
        self.listeclients.append(clt)

    def lirequantite(self,medicament):              # Méthode qu'on a ajouté, il vérifie si la quantité demandé est disponible dans le stock.Elle retourne une quantité(int)une fois on saisit une quantité valide
        quantite = int(input('Entrez la quantité désirée: '))
        while True :
            if quantite <= medicament.stock :
                return quantite
            else :
                m = medicament.stock
                print('Stock disponible: ',m)
            quantite = int(input('Quantité invalide, entrez la quantité désirée: '))

    @property
    def achat(self):                         # permet d'acheter un médicament avec toutes les opérations qu'entraine un achat
        client = self.lireclient             # vérifie si mon client est enregisté
        medicament = self.liremedicament     # vérifie si le médicament demandé est disponible
        quantite = self.lirequantite(medicament)             # vérifie si la quantité demandé est disponible
        somme = float(input('Saisir la somme: '))
        client.credit += -somme + quantite*medicament.prix   # modifie le crédit du client
        medicament.stock -= quantite                         # modifie la quantité du stock du médicament acheté

    @property
    def quitter(self):
        print('_____programme terminé!______')
