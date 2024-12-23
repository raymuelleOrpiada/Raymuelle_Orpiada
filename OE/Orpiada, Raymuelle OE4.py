class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacked {target.name} for {self.power} damage!")
        print(f"{target.name}'s remaining health: {target.health}")
    
    def special_move(self):
        pass

    def defend(self, attacker):
        damage = attacker.power // 2
        self.health -= damage
        print(f"{self.name} defended and took {damage} damage! Remaining health: {self.health}")

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2

class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball!")
        self.power = 100

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow!")
        self.power = 75

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50

warrior = Warrior("Warrior", 200, 30)
mage = Mage("Mage", 150, 25)
archer = Archer("Archer", 120, 20)
monster = Monster("Monster", 300, 15)

characters = [warrior, mage, archer, monster]

for character in characters:
    if isinstance(character, Character):
        character.attack(monster)
        character.special_move()

monster.defend(warrior)
monster.defend(mage)
monster.defend(archer)

for character in characters:
    if isinstance(character, Character) and character != monster:
        monster.attack(character)
        monster.special_move()
