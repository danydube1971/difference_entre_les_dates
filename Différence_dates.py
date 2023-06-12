"""Ce script Python permet de calculer la différence entre deux dates que l'utilisateur entre manuellement. Le script demande d'abord à l'utilisateur d'entrer une date de début et une date de fin au format JJ/MM/AAAA. Ensuite, le script utilise le module datetime pour calculer la différence entre les deux dates en termes de jours, de semaines, de mois et d'années.

Pour tenir compte des années bissextiles, le script utilise la fonction date du module datetime pour créer des objets date à partir des dates de début et de fin entrées par l'utilisateur. Ensuite, le nombre de jours, de semaines, de mois et d'années en différence est calculé en utilisant la différence entre ces objets date.

Enfin, le script affiche la différence entre les deux dates en termes de jours, de semaines, de mois et d'années à l'utilisateur. Le script est donc utile pour calculer la différence entre deux dates de manière précise et en tenant compte des années bissextiles."""


from datetime import date

# Fonction pour calculer la différence entre deux dates
def difference_dates(date_debut, date_fin):
    difference_jours = (date_fin - date_debut).days
    
    # Calculer le nombre d'années bissextiles entre les deux dates
    annees_bissextiles = 0
    for annee in range(date_debut.year, date_fin.year+1):
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
            annees_bissextiles += 1
    
    # Ajouter un jour pour chaque année bissextile entre les deux dates
    difference_jours += annees_bissextiles
    
    # Calculer le nombre de mois et d'années en utilisant le nombre total de jours
    difference_mois = difference_jours // 30
    difference_annees = difference_jours // 365
    
    return difference_jours, difference_mois, difference_annees

# Fonction pour demander à l'utilisateur d'entrer une date
def demander_date(message):
    while True:
        entree = input(message)
        try:
            jour, mois, annee = map(int, entree.split("/"))
            return date(annee, mois, jour)
        except ValueError:
            print("Format de date incorrect. Veuillez réessayer.")

# Demander à l'utilisateur d'entrer les dates de début et de fin
print("Calcul de la différence entre deux dates")
print("---------------------------------------")
date_debut = demander_date("Entrer une date de début (JJ/MM/AAAA) : ")
date_fin = demander_date("Entrer une date de fin (JJ/MM/AAAA) : ")


# Calculer la différence entre les deux dates
difference_jours, difference_mois, difference_annees = difference_dates(date_debut, date_fin)

# Calculer le nombre de semaines en utilisant le nombre total de jours
difference_semaines = difference_jours // 7

# Afficher la différence entre les deux dates
print("---------------------------------------")
print("Différence entre la date de début et la date de fin : ")
print("En jours : ", difference_jours)
print("En semaines : ", difference_semaines)
print("En mois : ", difference_mois)
print("En années : ", difference_annees)


