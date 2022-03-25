# Devoir 2 ift2015 - fait par henri-Cedric

'''
Prenom et nom :

(si vous travaillez en equipe)

Prenom et nom :

'''

import math
from io import StringIO
from os import remove

## !!  Ne pas modifier !! ##
'''
La classe Patient() represente un noeud de l'arbre (le Tas).
'''
class Patient:

    ## !!  Ne pas modifier !! ##
    '''
    Constructeur de la classe qui permet d'initialiser les variables d'instances.

    parametre :
        var_id : Id du patient (String)
        var_age : age du patient (entier)
    sortie : NA
    '''
    def __init__(self,var_id,var_age):
        self.id = var_id
        self.age = var_age

    ## !!  Ne pas modifier !! ##
    '''
    Permet de modifier l'age d'un patient
    parametre : new_age (entier)
    sortie : NA
    '''
    def change_age_patient(self, new_age):
        self.age = new_age

    ## !!  Ne pas modifier !! ##
    '''
    Permet d'afficher les informations du patient
    parametre : NA
    sortie : NA
    '''
    def affiche_patient(self):
        print('ID : '+ self.id +" -> age : "+str(self.age))


## !!  Ne pas modifier !! ##
'''
La classe Clinique() represente l'arbre (le Tas).
'''
class Clinique():

    ## !!  Ne pas modifier !! ##
    '''
    Constructeur de la classe qui permet d'initialiser les variables d'instances.

    parametre : NA
    sortie : NA
    '''
    def __init__ (self):
        self.data = []


    ## !!  Ne pas modifier !! ##
    '''
    retourne la position dans le tableau du noeud parent du noeud a la position j
    parametre : j est une position dans le tableau data (entier)
    sortie : entier
    '''
    def parent(self, j):
        return (j-1)//2


    ## !!  Ne pas modifier !! ##
    '''
    retourne la position dans le tableau de l'enfant de gauche du noeud a la position j
    parametre : j est une position dans le tableau data (entier)
    sortie : entier
    '''
    def left(self, j):
        return 2*j+1


    ## !!  Ne pas modifier !! ##
    '''
    retourne la position dans le tableau de l'enfant de droite du noeud a la position j
    parametre : j est une position dans le tableau data (entier)
    sortie : entier
    '''
    def right(self, j):
        return 2*j+2

    ## !!  Ne pas modifier !! ##
    '''
    retourne True si le noeud a la position j a un enfant a gauche
    parametre : j est une position dans le tableau data (entier)
    sortie : Boolean
    '''
    def has_left(self, j):
        return self.left(j) < len(self.data)

    ## !!  Ne pas modifier !! ##
    '''
    retourne True si le noeud a la position j a un enfant a droite
    parametre : j est une position dans le tableau data (entier)
    sortie : Boolean
    '''
    def has_right(self, j):
        return self.right(j) < len(self. data)


    ## !!  Ne pas modifier !! ##
    '''
    retourne True si le Tas est vide
    parametre : NA
    sortie : Boolean
    '''
    def is_empty(self):
        return len(self.data)==0

    ## !!  Ne pas modifier !! ##
    '''
    Cette methode permet d'inverser deux noeud dans le Tas
    parametre : i et j sont des positions dans le tableau (entier)
    sortie : NA
    '''
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]



    '''
    TODO :
     completer les fonctions necessaires a la simulation

     Vous pouvez rajouter vos fonctions dans cette partie

    '''

#========================================================================================================================================================================================================

    '''
    Cette methode permet d'ajouter un patient dans le Tas
    parametre :
        id : Id du patient que l'on souhaite ajouter (String)
        age : age du patient que l'on souhaite ajouter (entier)
    sortie : NA
    '''
    def add(self, id, age):
        patient = Patient(id, age)
        self.data.append(patient)
        self.upheap(len(self.data)-1)
        

    '''
    Cette methode permet, apres l'ajout d'un element, de conserver les propriete de l'ordre du Tas
    parametre : j est un entier
    sortie : NA
    '''
    def upheap(self, j):
        #j is root node
        if j == 0:
            return
        #get parent
        par = self.parent(j)
        #nage vers le haut recursivement
        if self.data[par].age < self.data[j].age:
            self.swap(par, j)
            self.upheap(par)
        else:
            return



    '''
    Cette methode permet, apres le retrait d'un element, de conserver les propriete de l'ordre du Tas
    parametre : j est un entier
    sortie : NA
    '''
    def downheap(self, j):
        leaf = self.data.pop()
        if self.is_empty():
            return
        self.data[j] = leaf
        while True:
            if self.biggestChild(j) == False:
                #j is a leaf
                return
            else:
                if (self.data[j].age > 
                self.data[self.biggestChild(j)].age):
                    return
                temp = self.biggestChild(j)
                self.swap(j, self.biggestChild(j))
                j = temp
                

    #added         
    def biggestChild(self, j):
        if self.has_left(j) and self.has_right(j):
            if self.data[self.left(j)].age > self.data[self.right(j)].age:
                return self.left(j)
            else:
                return self.right(j)
        elif self.has_left(j):
            return self.left(j)
        elif self.has_right(j):
            return self.right(j)
        else:
            return False

            
    '''
    retourne la position dans le tableau de l'element ayant l'id recu en parametre
    parametre :
        id : Id du patient (String)
    sortie : entier (retourne -1 si aucun element n'a ete trouve)
    '''
    def find(self,id):
        c=0
        for i in self.data:
            if i.id == id:
                return c
            c+=1
        return -1


    '''
    Permet de modifier l'age d'un patient
    Attention cette methode fait appel a la methode change_age_patient() de la classe Patient
    parametre :
            patient_id : Id du patient (String)
            new_age : l'age du patient (entier)
    sortie : NA
    '''
    def change_age(self,patient_id,new_age):
        j = self.find(patient_id)
        #change age of the patient
        self.data[j].change_age_patient(new_age)
        #delete then, add patient back
        patient = self.remove_element(j)
        self.add(patient.id, patient.age)


    '''
    retire et retourne l'element du Tas qui se trouve a l'indice recu en parametre
    parametre : l'indice de l'element qui doit etre retire (entier)
    sortie : Une instance de la classe Patient (l'element qui a ete retire)
    '''
    def remove_element(self,indice):
        element = self.data[indice]
        self.downheap(indice)
        return element


    '''
    retourne sans retirer les K elements maximum du Tas (avec les plus grande priorite)
    parametre : K est le nombre d'element qu'on on souhaite (entier)
    sortie : Un tableau qui contient les K elements maximum du Tas
    '''
    def top_k(self,k):
        tab = []
        for i in range(k):
            tab.append(self.remove_max())
        for j in tab:
            self.add(j.id, j.age)
        return tab

        


    '''
    retire et retourne les K elements maximum du Tas (avec les plus grande priorite)
    parametre : K est le nombre d'element qu'on on souhaite (entier)
    sortie : Un tableau qui contient les K elements maximum du Tas
    '''
    def pop_k(self,k):
        tab = []
        for i in range(k):
            tab.append(self.remove_max())
        return tab


    '''
    retourne sans retirer l'element maximum du Tas (avec la plus grande priorite)
    parametre : NA
    sortie : Une instance de la classe Patient. (l'element max du Tas qui a ete retire)
    '''
    def max(self):
        if self.is_empty():
            return False
        else:
            temp = self.remove_element(0)
            self.add(temp.id, temp.age)
            return temp


    '''
    retire et retourne l'element maximum du Tas (avec la plus grande priorite)
    parametre : NA
    sortie : Une instance de la classe Patient. (l'element qui a ete retire du Tas)
    '''
    def remove_max(self):
        if self.is_empty():
            return False
        else:
            return self.remove_element(0)

#========================================================================================================================================================================================================
## !!  Ne pas modifier !! ##
'''
Cette fonction permet d'afficher le Tas
parametre : tree est une instance de la classe Clinique
sortie : NA
'''
def show_tree(tree):
    total_width=60
    fill=' '
    output = StringIO()
    last_row = -1

    for i, n in enumerate(tree.data):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n.id).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)

    return


## !!  Ne pas modifier !! ##

'''
la fonction main permet de faire une simulation.
La correction se bassera sur l'execution de ce main
'''

def main():
    heap = Clinique()

    print(" Tas -->")
    show_tree(heap)

    print('On ajoute 2 patients')
    heap.add('A8932',12)
    heap.add('A1328',89)

    print(" Tas -->")
    show_tree(heap)

    print('\n\nOn cherche le patient le plus vieux')
    print('Voici le patient le plus vieux')
    temp = heap.max()
    temp.affiche_patient()

    print('\n\nOn ajoute 5 autres patients')

    heap.add('A2422',17)
    heap.add('A1210',87)
    heap.add('A1324',54)
    heap.add('A2330',24)
    heap.add('A1333',32)
    print(" Tas -->")
    show_tree(heap)

    print('\n\nOn retire le patient le plus vieux')
    print('Voici le patient qui a ete retire')
    temp = heap.remove_max()
    temp.affiche_patient()
    print(" Tas -->")
    show_tree(heap)


    print('\n\nOn cherche les 4 patients les plus vieux')
    temps = heap.top_k(4)
    print('Voici les 4 patients les plus vieux')
    for i in temps:
        i.affiche_patient()
    print(" Tas -->")
    show_tree(heap)

    pos = heap.find(temps[len(temps)-1].id)
    print("\n\nUne erreur a ete produite sur l'age du  4ieme patient le plus vieux qui est a la position : "+str(pos))
    temp = heap.change_age(temps[len(temps)-1].id,37)
    print(" Tas -->")
    show_tree(heap)

    print('\n\nOn ajoute 2 autres patients')
    heap.add('A2232',92)
    heap.add('A2213',7)
    print(" Tas -->")
    show_tree(heap)


    print('\n\nOn retire les 3 patients les plus vieux')
    temps = heap.pop_k(3)
    print('Voici les 3 patients les plus vieux')
    for i in temps:
        i.affiche_patient()
    print(" Tas -->")
    show_tree(heap)


    print('\n\nOn cherche les 2 patients les plus vieux')
    temps = heap.top_k(2)
    print('Voici les 2 patients les plus vieux')
    for i in temps:
        i.affiche_patient()
    print(" Tas -->")
    show_tree(heap)

    pos = heap.find(temps[0].id)
    print("\n\nOn retire le 1ieme patient le plus vieux")
    temp = heap.remove_element(pos)
    print(" Tas -->")
    show_tree(heap)

main()


'''
 Tas -->

------------------------------------------------------------
On ajoute 2 patients
 Tas -->
                           A1328
            A8932
------------------------------------------------------------


On cherche le patient le plus vieux
Voici le patient le plus vieux
ID : A1328 -> age : 89


On ajoute 5 autres patients
 Tas -->

                           A1328
            A1210                         A1333
     A8932          A1324          A2422          A2330
------------------------------------------------------------


On retire le patient le plus vieux
Voici le patient qui a ete retire
ID : A1328 -> age : 89
 Tas -->

                           A1210
            A1324                         A1333
     A8932          A2330          A2422
------------------------------------------------------------


On cherche les 4 patients les plus vieux
Voici les 4 patients les plus vieux
ID : A1210 -> age : 87
ID : A1324 -> age : 54
ID : A1333 -> age : 32
ID : A2330 -> age : 24
 Tas -->

                           A1210
            A1324                         A1333
     A2330          A2422          A8932
------------------------------------------------------------


Une erreur a ete produite sur l'age du  4ieme patient le plus vieux qui est a la position : 3
 Tas -->

                           A1210
            A1324                         A2330
     A2422          A8932          A1333
------------------------------------------------------------


On ajoute 2 autres patients
 Tas -->

                           A2232
            A1324                         A1210
     A2422          A8932          A1333          A2330
 A2213
------------------------------------------------------------


On retire les 3 patients les plus vieux
Voici les 3 patients les plus vieux
ID : A2232 -> age : 92
ID : A1210 -> age : 87
ID : A1324 -> age : 54
 Tas -->

                           A2330
            A2422                         A1333
     A2213          A8932
------------------------------------------------------------


On cherche les 2 patients les plus vieux
Voici les 2 patients les plus vieux
ID : A2330 -> age : 37
ID : A1333 -> age : 32
 Tas -->

                           A2330
            A1333                         A2422
     A8932          A2213
------------------------------------------------------------


On retire le 2ieme patient le plus vieux
 Tas -->

                           A1333
            A2422                         A8932
     A2213
------------------------------------------------------------

'''
