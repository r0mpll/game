#Абстрактный класс, от которого идет наследование классов Enemy,Physics,Magic,Hero
class Human():  
    mana=0
    hp=0
    damage=0
    lvl=1
    def lvlUp(self):
        self.lvl+=1

    def attack(self,isAggresive):
        if(isAggresive):   
            pass


human = Human()
human.lvlUp()
human.lvlUp()
human.lvlUp()
print(human.lvl)