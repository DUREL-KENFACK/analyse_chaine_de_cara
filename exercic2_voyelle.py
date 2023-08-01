

def TestLettre(phrase):
    liste_voyelle = ['a', 'e', 'i', 'u', 'o'] # liste des voyelles
    liste_consonne = [chr(i) for i in range(97,123)]  # liste des consonnes mais conntenant les voyelles aussi

    #supprimer les voyelles dans l'alphabet ou dans liste_consonne...
    for lettre in liste_consonne:
        if lettre in liste_voyelle:
            liste_consonne.remove(lettre)
    nombre_voyelle = 0
    nombre_consonne = 0

    for lettre in phrase:
        if lettre in liste_voyelle :
            nombre_voyelle +=1
        else:
            if lettre in liste_consonne:
                nombre_consonne +=1
    print(f'Nombre de voyelle : {nombre_voyelle}')
    print(f'Nombre de consonne : {nombre_consonne}')

    return 'Merci ...'

phrase = input('Entrez une phrase : ')
print(TestLettre(phrase))

