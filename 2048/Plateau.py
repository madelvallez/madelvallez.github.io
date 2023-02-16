from random import randint, choice
import Bloc

class Plateau:
    def __init__(self, dim:int):
        self.grille = [[None for i in range(dim)]for j in range(dim)]
        self.dim = dim
        self.apparition()
        self.apparition()

    def __str__(self) -> str:
        res = ""
        for i in range(self.dim):
            res += "["
            for j in range (self.dim-1):
                if self.grille[i][j] is None: 
                    res = res + " _\t"
                else :
                    res = res + " "+ str(self.grille[i][j]) + "\t"
            if self.grille[i][self.dim -1] is None:
                res = res + " _ ] \n"
            else:
                res = res + " " + str(self.grille[i][self.dim-1]) + " ] \n"
        return res
    

    def libres(self):
        '''renvi la liste des cases libres (==None)'''
        res = list()
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grille[i][j] is None:
                    res.append((i,j))
        return res

    def apparition(self):       #génère un bloc 2 ou 4 à une place libre
        libres = self.libres()
        (x,y) = choice(libres)
        choix_num =randint(0,9)
        if choix_num>0 : num=2  # si c'est pas 0, on met un 2
        else : num = 4          # sinon on met un 4
        self.grille[x][y] = Bloc.Bloc(num, (x,y))

    def est_vide_droite(self, coord): # bool selon que la case à droite est vide ou pas
        (x,y) = coord
        if y== self.dim :return False
        return self.grille[x][y+1] is None

    def est_vide_gauche(self, coord):
        (x,y) = coord
        if y==0 : return False
        return self.grille[x][y-1] is None

    def est_vide_haut(self, coord):
        (x,y) = coord
        if x==0 : return False
        return self.grille[x-1][y] is None

    def est_vide_bas(self,coord):
        (x,y) = coord 
        if x== self.dim : return False
        return self.grille[x+1][y] is None

    def deplacer(self, coord1, coord2): 
        '''Déplace le bloc en coordonnées coord2 dans la case coord2 si c'est possible'''
        x1,y1 = coord1
        x2, y2 = coord2
        assert self.grille[x1][y1] is not None , "il n'y a pas de bloc ici" 
        assert self.grille[x2][y2] is None, "il y a deja un bloc ici"
        self.grille[x1][y1].deplacer(x2,y2)
        self.grille[x2][y2] = self.grille[x1][y1]
        self.grille[x1][y1] = None

    #---- DECALER VERS DROITE -----------------------------------------------------
    def bloc_plus_proche_gauche(self, coord):
            '''prend les coordonnées d'une case du plateu et 
            renvoie les coordonnée du bloc le plus proche à gauche (lui mm inclus) 
                    et None sinon '''
            (i,j) = coord
            assert (0<= i < self.dim) and (0 <= j < self.dim), "Coordonnées interdites"+str(i)+","+str(j)
            while(j>=0):
                if self.grille[i][j] is None:
                    j -= 1
                else:
                    return (i,j)
            return None

    def decaler_droite(self):
        '''décale tout les bloc le plus a droite possible'''
        for i in range(self.dim):
            for j in range(self.dim-1, -1, -1):
                if self.grille[i][j] is None:
                    bientot = self.bloc_plus_proche_gauche((i,j))
                    if bientot is not None:
                        self.deplacer(bientot, (i,j))
    
    def fusion_droite(self):
        '''effectue les fusions possible vers la droite'''
        for i in range(self.dim): # pour chaque ligne
            for j in range(self.dim-1, 0, -1): #pour chaque case de gauche à droite sauf la dernière
                b1 = self.grille[i][j]
                b2 = self.grille[i][j-1]
                if b1 is not None and b2 is not None and b1.fusion_legale(b2):
                    b1.fusion(b2)
                    self.grille[i][j-1] = None

    def mouvement_droite(self):
        '''effectue les opérations pour obtenir le plateau 
        après un mouvement vers la droite'''
        self.decaler_droite()
        self.fusion_droite()
        self.decaler_droite()
        self.apparition()



#---- DECALER VERS gauche -----------------------------------------------------
    def bloc_plus_proche_droite(self, coord):
            '''prend les coordonnées d'une case du plateau et 
            renvoie les coordonnée du bloc le plus proche à droite (lui mm inclus) 
                    et None sinon '''
            (i,j) = coord
            assert (0<= i < self.dim) and (0 <= j < self.dim), "Coordonnées interdites"+str(i)+","+str(j)
            while(j< self.dim):
                if self.grille[i][j] is None:
                    j += 1
                else:
                    return (i,j)
            return None

    def decaler_gauche(self):
        '''décale tout les bloc le plus a gauche possible'''
        for i in range(self.dim):
            for j in range(self.dim):
                if self.grille[i][j] is None:
                    bientot = self.bloc_plus_proche_droite((i,j))
                    if bientot is not None:
                        self.deplacer(bientot, (i,j))
    
    def fusion_gauche(self):
        '''effectue les fusions possible vers la gauche'''
        for i in range(self.dim): # pour chaque ligne
            for j in range(self.dim-1): #pour chaque case de droite à gauche sauf la dernière
                b1 = self.grille[i][j]
                b2 = self.grille[i][j+1]
                if b1 is not None and b2 is not None and b1.fusion_legale(b2):
                    b1.fusion(b2)
                    self.grille[i][j+1] = None

    def mouvement_gauche(self):
        '''effectue les opérations pour obtenir le plateau 
        après un mouvement vers la gauche'''
        self.decaler_gauche()
        self.fusion_gauche()
        self.decaler_gauche()
        self.apparition()

#---- DECALER VERS bas -----------------------------------------------------
    def bloc_plus_proche_haut(self, coord):
            '''prend les coordonnées d'une case du plateau et 
            renvoie les coordonnée du bloc le plus proche en haut (lui mm inclus) 
                    et None sinon '''
            (i,j) = coord
            assert (0<= i < self.dim) and (0 <= j < self.dim), "Coordonnées interdites"+str(i)+","+str(j)
            while(i >= 0):
                if self.grille[i][j] is None:
                    i -= 1
                else:
                    return (i,j)
            return None

    def decaler_bas(self):
        '''décale tout les bloc le plus en bas possible'''
        for j in range(self.dim):
            for i in range(self.dim-1, -1, -1):
                if self.grille[i][j] is None:
                    bientot = self.bloc_plus_proche_haut((i,j))
                    if bientot is not None:
                        self.deplacer(bientot, (i,j))
    
    def fusion_bas(self):
        '''effectue les fusions possible vers le bas'''
        for j in range(self.dim): # pour chaque ligne
            for i in range(self.dim-1, 0, -1): #pour chaque case de bas en haut sauf la dernière
                b1 = self.grille[i][j]
                b2 = self.grille[i-1][j]
                if b1 is not None and b2 is not None and b1.fusion_legale(b2):
                    b1.fusion(b2)
                    self.grille[i-1][j] = None

    def mouvement_bas(self):
        '''effectue les opérations pour obtenir le plateau 
        après un mouvement vers le bas'''
        self.decaler_bas()
        self.fusion_bas()
        self.decaler_bas()
        self.apparition()


#---- DECALER VERS haut -----------------------------------------------------
    def bloc_plus_proche_bas(self, coord):
            '''prend les coordonnées d'une case du plateau et 
            renvoie les coordonnée du bloc le plus proche en bas (lui mm inclus) 
                    et None sinon '''
            (i,j) = coord
            assert (0<= i < self.dim) and (0 <= j < self.dim), "Coordonnées interdites"+str(i)+","+str(j)
            while(i < self.dim):
                if self.grille[i][j] is None:
                    i += 1
                else:
                    return (i,j)
            return None

    def decaler_haut(self):
        '''décale tout les bloc le plus en haut possible'''
        for j in range(self.dim):
            for i in range(self.dim):
                if self.grille[i][j] is None:
                    bientot = self.bloc_plus_proche_bas((i,j))
                    if bientot is not None:
                        self.deplacer(bientot, (i,j))
    
    def fusion_haut(self):
        '''effectue les fusions possible vers le haut'''
        for j in range(self.dim): # pour chaque ligne
            for i in range(self.dim-1): #pour chaque case de bas en haut sauf la dernière
                b1 = self.grille[i][j]
                b2 = self.grille[i+1][j]
                if b1 is not None and b2 is not None and b1.fusion_legale(b2):
                    b1.fusion(b2)
                    self.grille[i+1][j] = None

    def mouvement_haut(self):
        '''effectue les opérations pour obtenir le plateau 
        après un mouvement vers le haut'''
        self.decaler_haut()
        self.fusion_haut()
        self.decaler_haut()
        self.apparition()
