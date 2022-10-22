
class Spell():
    manacost=0
    damage=0
    recoil=0
    range=0
    isStudied=False
    isAvaible=False
    lvl=0
    maxLvl=4
    minLvlForStuding=1
    def lvlUp(self,lvl):
        if(lvl>=self.minLvlForStuing and self.lvl<self.maxLvl):
            self.lvl+=1
            self.isStudied=True
            if(self.lvl==1):
                self.isAvaible=True
    def recoil(self):
        pass
    def use(self):
        if(isAvaible):
            isAvaible=False
