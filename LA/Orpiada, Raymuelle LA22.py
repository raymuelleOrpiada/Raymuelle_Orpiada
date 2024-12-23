class BirthdayParty:
    def __init__(self, theme, foods):
        self.theme = theme
        self.foods = foods
        self.__secret_dish = "Surprise Cake!"

    def print_party_details(self):
        print(f"Party Theme: {self.theme}")
        print("Foods:")
        for food in self.foods:
            print(f"- {food}")
        self.__print_secret_dish()

    def __print_secret_dish(self):
        print(f"Secret Dish: {self.__secret_dish}")

party1 = BirthdayParty("Jungle Adventure", ["Fruit Skewers", "Mini Pizzas", "Animal Crackers"])
party2 = BirthdayParty("Unicorn Dreams", ["Rainbow Cupcakes", "Cotton Candy", "Sparkling Lemonade"])
party3 = BirthdayParty("Pirate Treasure", ["Treasure Hunt Cookies", "Goldfish Crackers", "Fruit Salad"])

party1.print_party_details()
print()
party2.print_party_details()
print()
party3.print_party_details()