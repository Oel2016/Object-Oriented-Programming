#il s'agit du jeu de test.pour vérifier notre programme, Merci de suivre les étapes suivantes
#pour afficher le menu , Tapez start() depuis le terminal
#on a déja créé une pharmacie ci-dessous qui s'appelle bouskoura , ainsi que deux clients et deux médicaments
# il suffit de taper le numéro de l'opération que vous souhaitez effectuer et suivre les opérations demandé depuis le terminal
#Merci de nommer, le fichier python ou vous allez faire l'execution , Gestion_de_pharmacie_app pour importer les classes.

from Gestion_de_pharmacie_app import client,medicament,pharmacie                    #Merci de nommer, le fichier python ou vous allez faire l'execution , Gestion_de_pharmacie_app
# les clients
ibrahim = client('ibrahim',-300)   créer
omar = client('omar',300)
#les medicaments
doliprane = medicament('doliprane',20,500)
aspirine = medicament('aspirine',50,400)
#liste clients
listeclient = [ibrahim , omar]
#liste medicaments
listemedicament = [doliprane , aspirine]
#nortre pharmacie
bouskoura = pharmacie(listeclient,listemedicament)

def start():                                               # affichage du Menu
    print('1 : Achat de médicament')
    print('2 : Approvisionnement en  médicaments')
    print('3 : Affichage des stocks et des crédits')
    print('4 : Enregistrement médicament')
    print('5 : Enregistrement client')
    print('6 : Quitter')
    L=[1,2,3,4,5,6]
    choix = 0
    while True :
        i = int(input("Veuillez choisir l'option que vous souhaitriez exécuter: "))  # choisir une opération
        if i in L:
            choix = i                                                                # chaque opération correspond à un numéro affiché au départ
            break

    if choix == 1:                                                                   # achat
        bouskoura.achat
    if choix == 2:                                                                   # approvisionnement
        bouskoura.approvisionnement
    if choix == 3:                                                                   # affichage des clients et leurs crédits  et des médicaments et leurs stocks de la pharmacie
        bouskoura.affichage
    if choix == 4:                                                                   # enregistrement d'un médicament
        bouskoura.enregistrement
    if choix == 5:                                                                   # enregistrement d'un client
        bouskoura.enregistrement_client
    if choix == 6:                                                                   #quitter
        bouskoura.quitter





