import csv


def importer_donnees():
    data = (open('DATABASE/notes.csv', mode='r'))
    data.readline()
    k = []
    for l in data:
        line = l.split(',')
        d = {'ID': line[0],
             'Nom': line[1],
             'Prenom': line[2],
             'MD01': line[3],
             'Note': float(line[4]),
             }
        k.append(d)
    """print(data)
    lire le fichier notes.csv
    :return: liste étudiants
    """
    return k


def calculer_moyenne_etudiants(k=[]):
    x = []
    for dic in k:
        index = -1
        for i in range(len(x)):
            e = k[i]
            if e['ID'] == dic['ID']:
                index = i
        if index == -1:
            x.append({
                'ID': dic['ID'],
                'Nom': dic['Nom'],
                'Prenom': dic['Prenom'],
                'Notes': [float(dic['Note'])]
            }
            )
        else:
            x[i]['Notes'].append(dic['Note'])
    for e in x:
        note = e['Notes']
        v = 0
        moyene = 1
        for i in note:
            v += i
        moyene = v / len(note)
        e['moyenne'] = moyene
    """
    calcule la moyenne de chaque étudiant
    :param list_etudiants:
    :return: liste étudiants avec moyenne.
    """
    return x


def calculer_moyenne_globale(x=[]):
    s = 0
    for e in x:
        s += e['moyenne']
    if len(x) == 0:
        return 0
    else:
        return s/len(x)
    """
    calcule la moyenne globale de la classe
    :param list_moyennes:
    :return: moyenne globale de classe.
    """


def ecrire_resultats(list_moyennes,moyenneg):
    filename = 'moyeens_file.csv'
    fields = ['ID','Nom','Prenom','Notes','moyenne','Moyenne General']
    for e in list_moyennes:
        e['Moyenne General'] = moyenneg
        break
    with open(filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for e in list_moyennes:
            writer.writerow(e)

    # écrit les résultats dans le fichiers résultats.csv.
    # :param list_moyenes:
    # :param mg:
    # :return:
    # """
    # pass


list_etudiants = importer_donnees()
# print(importer_donnees())
list_moyennes = calculer_moyenne_etudiants(list_etudiants)
print(list_moyennes)
moyenneg = calculer_moyenne_globale(list_moyennes)
# print(mg)
result = ecrire_resultats(list_moyennes,moyenneg)
print(result)