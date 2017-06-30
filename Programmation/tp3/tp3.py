#Annés bissextiles

def est_divisible_par(a,b):
    return a % b == 0
def est_bissextile(annee):
    return est_divisible_par(annee,4) and not est_divisible_par(annee,1000) or est_divisible_par(annee,400)
#Nombre de jours dans un mois

def nbre_jour(m,a):
    '''    1,3,5,7,8,10,12 => 31
    4,6,9,11 => 30
    2 => 29 ou 28'''
    
    '''Trouvez un moyen pour supprimer les if'''
    '''try:
        assert m > 0 and m < 13'''
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if not est_bissextile(a) and m == 2:
        return 28
    if est_bissextile(a) and m == 2:
        return 29
    '''except AssertionError:
        print("La valeur doit être comprise entre 1 et 12")'''

for i in range(1,12):
    print(nbre_jour(i,2014))

print(nbre_jour(2,2016))
print(nbre_jour(0,2016))
print()
print()



#assert

''' m = -1  renvoie None'''
'''  if m > 0 and m < 13'''
'''  assert permet de faire une tester une valeur et de crée une exception'''

#Date valide

def est_date_valide(j,m,annee):
    '''tester le mois puis le nombre de jour'''
    return j == nbre_jour(m,annee) and (m > 0 and m < 13)

print(est_date_valide(1,13,2014))
print(est_date_valide(29,2,2016))
print(est_date_valide(32,1,2014))
print()
print()

#Numéro du jour dans la semaine




def corrige_mois(m,annee):
    mois = [4,6,0,3,5,1,3,6,2,4,0,2]
    if(est_bissextile(annee)):
        mois[0] = 3
        mois[1] = 0
    return mois

def num_jour(j,m,annee):
    '''Formule Delambre : k + q +cd +M+ Q + 2 + 5 * ab
    k = 2ème partie de l'année divisé par 4
    q = 1ème partie de l'année divisé par 4
    cd =2ème partie de l'année
    Q= jour
    M=mois
    ab = 1er partie de l'année'''
    k = (annee % 100//4)
    q = (annee // 100 // 4)
    cd = annee % 100
    Q = j
    M = corrige_mois(m,annee)[m-1]
    ab = annee //100
    return (k + q + cd + M + Q + 2 + 5 * ab) % 7

def nom_jour(j,m,annee):
    jour = ["Dimanche","Lundi","Mardi","Mecredi","Jeudi","Vendredi","Samedi"]
    return jour[num_jour(j,m,annee)]




#Imprimer le calendrier d’un mois

print("toto")
print()
print()

def nom_mois(n):
    l = ['janvier', 'février', 'mars', 'avril',
     'mai', 'juin', 'juillet', 'août',
     'septembre', 'octobre', 'novembre', 'décembre']
    return l[n-1]


def imprimer_mois(m,annee):

    
    
        
   
imprimer_mois(9,2014)
