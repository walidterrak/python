# # Demander à l'utilisateur de saisir un nombre entier positif
# nombre = int(input("nombre entier."))

# # Vérifier si le nombre est positif
# if nombre > 0:
#     # Boucle pour afficher tous les nombres de 1 à 'nombre'
#     for i in range(1, nombre + 1):
#         print(i)
# else:
#     print("nombre entier.")


# Demander à l'utilisateur de saisir un nombre entier positif
# def filtrer_nombres_positifs(liste):
#     # Utiliser une compréhension de liste pour filtrer les nombres positifs
#     return [nombre for nombre in liste if nombre > 0]

# # Exemple d'utilisation
# liste_nombres = [-5, 3, -1, 7, 0, -2, 9]
# nombres_positifs = filtrer_nombres_positifs(liste_nombres)
# print(nombres_positifs)

# def filtres_mots_voyelles(liste):
#     voyelles = ['a','e','i','o', 'u']
#     return [mots for mots in liste if mots[0].lower() in voyelles]

# liste = ["arbre","voiture","couscous","oiseau","univers"]
# mots_voyelles = filtres_mots_voyelles(liste)
# print(mots_voyelles)   

# mot = str(input("mots"))
# if len(mot) > 5:
#     print("ok !")
# else:
#     print("no !")

nombres = [int(input("nombres entiers:")) for _ in range(5)]

print("les nombres sont :", nombres)
