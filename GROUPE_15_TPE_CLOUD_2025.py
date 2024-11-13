def reduction_par_paires(liste):
    """
    Réduit une liste de nombres en additionnant chaque paire consécutive d'éléments
    jusqu'à ce qu'il ne reste qu'un seul élément.

    :param liste: Liste d'entiers ou de flottants
    :return: Une liste contenant un entier ou flottant représentant la somme réduite
    """
    # Tant que la liste a plus d'un élément, on continue la réduction
    while len(liste) > 1:
        nouvelle_liste = []
        
        # Itérer sur la liste par paires (deux éléments à la fois)
        for i in range(0, len(liste), 2):
            # Si c'est une paire complète (deux éléments), on additionne
            if i + 1 < len(liste):
                somme = liste[i] + liste[i + 1]
                nouvelle_liste.append(somme)
            else:
                # S'il reste un élément non apparié, on le conserve tel quel
                nouvelle_liste.append(liste[i])
        
        # Mise à jour de la liste pour la prochaine itération
        liste = nouvelle_liste
        print(f"Étape intermédiaire: {liste}")  # Afficher les étapes intermédiaires

    # À la fin, la liste contiendra un seul élément
    return liste[0]

# Exemple d'utilisation
resultat = reduction_par_paires([1,1,3,7,9,7,3])