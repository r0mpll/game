from human import Human
class Enemy(Human):
    isAggresive=False
    def getAggresive(self):
        return self.isAggresive

    def setAggresive(self,aggresive):
        self.isAggresive=aggresive
        

