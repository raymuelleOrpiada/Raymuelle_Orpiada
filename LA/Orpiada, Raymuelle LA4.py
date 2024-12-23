class MobileLegendHero:
    def __init__(self, hero_name):
        self.hero_name = hero_name

    def __str__(self):
        return f"{self.hero_name} is a marksman hero." 

mm = MobileLegendHero("Moskov")
print(mm) 