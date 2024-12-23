class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            result = func(*args, **kwargs)
            print("This character is amazing!")
            return result
        return wrapper

naruto = AnimeCharacter("Naruto", "Shadow Clone Jutsu")


def character_intro():
    print(f"I am {naruto.name} and I can use {naruto.ability}.")


character_intro = naruto.introduce(character_intro)


character_intro()