class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        print(f"{target.name}'s health is now {target.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} health!")
        print(f"{self.name}'s health is now {self.health}")

player1 = Player("Yasuo", 100, 20)
player2 = Player("Zed", 150, 15)

while True:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player1.name} wins!")
        break

    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player2.name} wins!")
        break