class MobileLegendHero:
    def __init__(self, hero_name):
        self.hero_name = hero_name

    def marksman(self):
        return f"{self.hero_name} is my cat." 

mm = MobileLegendHero("Sora")
print(mm.marksman()) 