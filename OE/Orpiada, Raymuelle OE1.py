class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} ({self.role}, {self.damage_type})"

    def describe(self):
        return f"{self.name} is a {self.role} with {self.damage_type} damage."


heroes = [
    Hero("Layla", "Marksman", "Physical"),
    Hero("Gusion", "Assassin", "Magic"),
    Hero("Tigreal", "Tank", "Physical"),
    Hero("Angela", "Support", "Magic"),
    Hero("Esmeralda", "Fighter", "Magic")
]

def describe_team(team):
    print("Mobile Legends Dream Team:")
    for hero in team:
        print(hero.describe())

describe_team(heroes)
