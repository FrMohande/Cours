Mercredi 2 décembre  - TP8 : Simulation d’un canal bruité, et codage correcteur d’erreur 

Outioua Mohand - Soleillet Jonathan 

Partie IV Codage de Hamming



IV)



L'encodage par répétitions (2 détecteur, 1 correcteur)  rendement 1/3 
L'encodage par Hamming (3 détecteurs, 1 correcteur )  rendement 1/2 

L'encodage par répétitions détectera toujours plus d'erreur que l'encodage par Hamming mais
Hamming corrigera autant d'erreur que l'encodage par répétitions.


Pour calculer la moyenne d'erreur : n*p

n = taille fichier après encodage en bits
p = probabilité d'erreurs

exemple :
pour repeat : (11961 * 8) * 0.001 = 95 erreurs moyenne
pour hamming : (7974 * 8) * 0.001 = 64 erreurs moyenne
