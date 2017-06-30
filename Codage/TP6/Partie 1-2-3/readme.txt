Mercredi 25 novembre  - TP6 : Simulation d’un canal bruité, et codage correcteur d’erreur 

Outioua Mohand - Soleillet Jonathan 

Partie I Le canal binaire symétrique sans mémoire :


II)
 
1. Si p est inférieur à 0 ou supérieur à 1 on lève l'exception "Not_a_proba"
Il faut que la valeur de p soit entre l'intervalle 0<=p<=1

2 Si n est inférieur à 0 ou supérieur à 255 on lève l'exception "Not_a_byte"
Il faut que la valeur de n soit entre l'intervalle 0<=n<=255


3. lorsque p=0, celà veut dire que le taux d'erreur ou bruit est de 0% donc le byte envoyait, a travers le canal, ne change pas.

>>> cbssm(0,255)
255
>>> cbssm(0,254)
254



4. Lorsque p = 1  celà veut dire erreur sur chaque bits., la valeur qu'on renvoie sera le résultat de 255 ^ bytes ( qu'on a mis en paramètre )  


Partie II CBSSM appliqué sur un fichier :


6.

pour p = 0.1 on a plus de 50% du fichier qui devient illisible
pour p = 0.05 on a 40% du fichier qui devient illisible 
pour p = 0.01 on a moins de 10% du fichier qui devient illisible 
pour p = 0.001 on a moins de 1% du fichier qui devient illisible 


7.


Non nous ne pouvons plus décompresser ce fichier produit.




III)


16. A partir de p > 10**-6, le fichier decodé devient incorrect
