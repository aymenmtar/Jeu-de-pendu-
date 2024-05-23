import random
from unicodedata import normalize


def lire_mots(fichier=None):
    mots_par_defaut = [
        "carbone", "mandat", "arbuste", "gommeux", "lyrique", "arnica", "moulure", "schisme", "turbot", "satire",
        "stupide", "veneneux", "argileux", "cathode", "froufrou", "affable", "foudroyant", "gambader", "heredite",
        "mythique", "pulsion", "balafre", "brimborion", "ciselure", "cynique", "dialecte", "insomniaque",
        "labyrinthique", "prosaique", "rubicond", "affront", "cobalt", "constat", "defrayer", "escompte", "fabuler",
        "fetiche", "freiner", "innover", "mandrin", "moiteur", "opulence", "sommeil", "truffade", "aplomb", "caprice",
        "celeste", "derober", "exulter", "fiabilite", "guetter", "impasse", "judicieuse", "laicite", "mortier",
        "panache", "relache", "serment", "surprenant", "abimer", "acarien", "courant", "creuser", "deriver",
        "embusque", "emprunt", "essaimer", "fantome", "foison", "gavroche", "guimauve", "jaspe", "lacune", "metayer",
        "anodin", "carnage", "cloitre", "colmater", "combler", "derisoire", "elaguer", "endurci", "etouffer",
        "fabuleux", "galopin", "gouffre", "harmonie", "larcin", "marasme", "abstrus", "alveole", "ancrage", "ardeur",
        "avatar", "cadence", "chignon", "dilater", "egratignure", "eminent", "exister", "fantaisie", "foudre",
        "goguenard", "hachoir", "inedit", "liquide", "metayer", "opaque", "parodie", "château", "éléphant", "noël",
        "étudiant", "hôpital", "crème", "résumé", "délicieux", "écriture", "pôle", "âge", "mélodie", "pièce", "forêt",
        "légume", "âge", "cliché"
    ]

    if fichier:
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                mots = f.read().split()
            return mots
        except FileNotFoundError:
            print(f"Le fichier {fichier} n'a pas été trouvé. Veuillez fournir un chemin valide.")
            fichier = input("Entrez le chemin vers votre fichier de mots ou pressez sur l'entrée pour jouer avec les mots par défauts: ").strip()
            return lire_mots(fichier)  # Répéter la fonction avec le nouveau chemin du fichier
    else:
        return mots_par_defaut


def normaliser(mot):
    return normalize('NFD', mot).encode('ASCII', 'ignore').decode('utf8')


def choisir_mot(mots):
    return random.choice(mots)


def afficher_mot(mot, lettres_devinees):
    return ' '.join([lettre if lettre in lettres_devinees else '_' for lettre in mot])


def demander_lettre():
    lettre = input("Devinez une lettre: ").strip().lower()
    return normaliser(lettre)


def jouer():
    utiliser_fichier = input("Voulez-vous utiliser un fichier personnalisé pour les mots ? (o/n): ").strip().lower()
    if utiliser_fichier == 'o':
        fichier = input("Entrez le chemin vers votre fichier de mots: ").strip()
        mots = lire_mots(fichier)
    else:
        mots = lire_mots()

    if not mots:
        print("Aucun mot disponible pour jouer.")
        return

    mot = choisir_mot(mots)
    mot_normalise = normaliser(mot)
    lettres_devinees = set()
    lettres_incorrectes = set()
    chances = 6

    while chances > 0:
        print(f"Mot: {afficher_mot(mot, lettres_devinees)}")
        print(f"Chances restantes: {chances}")
        print(f"Lettres incorrectes: {' '.join(lettres_incorrectes)}")

        lettre = demander_lettre()

        if lettre in lettres_devinees or lettre in lettres_incorrectes:
            print("Vous avez déjà deviné cette lettre.")
            continue

        if lettre in mot_normalise:
            lettres_devinees.add(lettre)
            if set(mot_normalise) == lettres_devinees:
                print(f"Félicitations ! Vous avez deviné le mot : {mot}")
                break
        else:
            lettres_incorrectes.add(lettre)
            chances -= 1
            if chances == 1:
                print("Indice: une lettre qui n'est pas dans le mot est ajoutée.")
                lettres_incorrectes.add(
                    random.choice([l for l in 'abcdefghijklmnopqrstuvwxyz' if l not in mot_normalise]))

        if chances == 0:
            print(f"Dommage, vous avez perdu. Le mot était : {mot}")

    rejouer = input("Voulez-vous rejouer ? (o/n): ").strip().lower()
    if rejouer == 'o':
        jouer()
    else:
        print("Merci d'avoir joué !")


if __name__ == "__main__":
    jouer()

