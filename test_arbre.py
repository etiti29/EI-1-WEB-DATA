
#créé le vocabluaire associé à l'ensemble des tweets sous la forme d'un dictionnaire qui associe à un mot une liste contenant son identifiant et sa fréquence dans la data
def vocabulaire(data):   
    voc={}                  
    i=0
    for tweet in data.values()[0]:
        mots=tweet[0].split()
        for i in range(len(mots)):
            if mots[i] in voc.keys():
                if mots[i] not in tweet[:i-1]:
                    voc[mots[i]][1]+=1
            else :
                voc[mots[i]]=[i,1]
                i+=1
    return voc
