from random import randint


#Compte à rebours

def compte_a_rebours(n):
    i = n 
    while i >= 0:
        print(i)
        i = i - 1
compte_a_rebours(10)

#Série Harmonique alternée

def somme_partielle(n):
    s = 0
    for i in range(1,n):
        s = ((-1) ** i // i) + s
    return s

print(somme_partielle(10))

#Tables de multiplication

def imprimer_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n * i)
imprimer_table(7)

'''for i in range(1,11):
    imprimer_table(i)'''

print()

#Suite arithmético-géomètrique

#2

def u_terme(n):
    u_0 = 0
    while n > 0 :
        s = 3 * u_0 + 1
        u_0 = s
        n = n - 1
    return s

print(u_terme(3))

#3


def atteint(m):
    s = 0
    n = 0
    while m >= s:
        n = n + 1
        s = 3 * s +1
    return n
print(atteint(41))


#Choisis un nombre

'''floor(random() * 10 + 1)) entre 1 et 10'''

#1 radint permet de prendre un nombre entier compris entre les deux bornes
# radint(1,10) nombre entre 1 et 10

#2
#input lecture de ce qu'on va écrire dans le cmd, les types sont en chaine
#int(input())

#5

'''def mystere():
    mystere = randint(1,100)
    n = 7 
    while n > 0:
        print("il vous reste", n, "essais")
        reponse = int(input("Veuillez écrire votre chiffre:"))
        if mystere == reponse:
            print("Vous avez gagné")
            break
        elif mystere > reponse:
            print("+")
            n = n - 1
        else:
            print("-")
            n = n - 1
    if n == 0:
        print("Vous avez perdu")

mystere()'''

#7
def mystere2():
    n = int(input("Combien voulez vous d'essai ?"))
    print("Vous allez choisir l'intervalle pour le chiffre mystere:")
    a = int(input("Choissiez votre 1er borne : "))
    b = int(input("Choissiez votre 2ème borne :"))
    if b > a:
        mystere = randint(a,b)
        while n > 0:
            print("il vous reste", n, "essais")
            reponse = int(input("Veuillez écrire votre chiffre:"))
            if mystere == reponse:
                print("Vous avez gagné")
                break
            elif mystere > reponse:
                print("+")
                n = n - 1
            else:
                print("-")
                n = n - 1
        if n == 0:
            print("Vous avez perdu")
            print("Le chiffre mystère était", mystere)
    else:
        print("Votre choix de borne est trop grand")
    
mystere2()
