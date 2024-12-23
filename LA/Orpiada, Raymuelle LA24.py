from abc import ABC, abstractmethod
class GameCharacter(ABC):
    @abstractmethod

    def attack(self):
        pass
    
class warrior(GameCharacter):
    def attack(self):
        print("Swing sword")

class mage(GameCharacter):
    def attack(self):
        print("Castt a fireball!")
        
class archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow")
    
warrior = warrior()
mage = mage()
archer = archer()

warrior.attack()
mage.attack()
archer.attack()   