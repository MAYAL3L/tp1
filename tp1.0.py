
import random

# Affichage de la bannière d'accueil
print("##############################################")
print("\nRecrutement - IFT -1004 Corp")
print("\n##############################################")

# Demande du nombre de candidatures
nombre_candidats = int(input("\nCombien de candidatures souhaitez-vous traiter ? "))

# Gestion du cas où le nombre de candidats est égal à zéro
if nombre_candidats == 0:
    print("\nAucun candidat à évaluer. Fin du programme.")
    exit()

# Initialisation des compteurs pour le bilan final
total_candidats = 0
candidats_retenus = 0
candidats_rejetes = 0

# Boucle pour traiter chaque candidat
for i in range(1, nombre_candidats + 1):
    print(f"\n============\nCandidat {i}/{nombre_candidats}\n============")

    # Entrée des informations du candidat
    nom = input("Nom : ")
    age = int(input("Âge : "))

    # Saisie du niveau d'études avec validation
    niveau_etudes = ""
    while niveau_etudes not in ("collegial", "baccalaureat", "maitrise", "doctorat"):
        niveau_etudes = input("Niveau d'études (collegial, baccalaureat, maitrise, doctorat) : ")
        if niveau_etudes not in ("collegial", "baccalaureat", "maitrise", "doctorat"):
            print("Niveau d'études invalide.")

    experience = int(input("Expérience professionnelle (années) : "))
    competences = int(input("Compétences techniques (sur 10) : "))

    # Calcul du score du candidat
    score = 0

    # Points en fonction de l'âge
    if 18 <= age <= 30:
        score += 10
    elif 31 <= age <= 45:
        score += 7
    else:
        score += 5

    # Points en fonction du niveau d'études
    if niveau_etudes == "doctorat":
        score += 10
    elif niveau_etudes == "maitrise":
        score += 8
    elif niveau_etudes == "baccalaureat":
        score += 6
    else:
        score += 4

    # Points en fonction de l'expérience professionnelle
    if experience >= 1 and experience <= 5:
        score += 5
    elif experience > 5:
        score += 10

    # Points en fonction des compétences techniques
    if competences >= 5 and competences <= 7:
        score += 5
    elif competences >= 8:
        score += 10

    # Composante aléatoire entre -5 et +5
    score += random.randint(-5, 5)

    # Décision : retenu ou rejeté
    total_candidats += 1
    if score >= 25:
        candidats_retenus += 1
        decision = "RETENU"
    else:
        candidats_rejetes += 1
        decision = "REJETÉ"

    print(f"\nDécision pour {nom} : {decision}")
    print(f"Score obtenu : {score} points")

# Calcul des taux de réussite et d'échec
if total_candidats > 0:
    taux_reussite = (candidats_retenus / total_candidats) * 100
    taux_echec = (candidats_rejetes / total_candidats) * 100
else:
    taux_reussite = 0
    taux_echec = 0

# Affichage du bilan final
print("\nRésumé du processus de recrutement :")
print(f"- Nombre total de candidats évalués : {total_candidats}")
print(f"- Nombre de candidats retenus pour entretien : {candidats_retenus}")
print(f"- Nombre de candidats rejetés : {candidats_rejetes}")
print(f"- Taux de réussite : {taux_reussite:.2f}%")
print(f"- Taux d'échec : {taux_echec:.2f}%")

print("\nFin du programme.")

