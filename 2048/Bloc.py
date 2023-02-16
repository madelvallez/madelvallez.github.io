class Bloc :
    def __init__(self,num:int, pos:tuple):
        self.num = num
        self.coord = pos
    
    def __str__(self):
        return str(self.num)
    
    def deplacer(self, dest):
        self.coord = dest

    def est_a_cote(self, bloc):
        x,y = self.coord
        a,b = bloc.coord
        if x==a and (y==b+1): return "gauche"
        if x==a and y==b-1 : return "droite"
        if (x==a+1) and y==b:return "haut"
        if x==a-1 and y==b : return "bas"
        return False

    def fusion_legale(self, bloc):
        '''prens deux bloc et renvoie true si ils sont fusionable'''
        return self.est_a_cote(bloc) and self.num==bloc.num

    def deplacer(self, x, y):
        self.coord=(x,y)

    def fusion(self, bloc):
        '''fudionne les deux bloc dans self 
        /!\ bloc n'est pas supprimé'''
        assert self.fusion_legale(bloc), "fusion illégale"
        self.num= self.num**2


