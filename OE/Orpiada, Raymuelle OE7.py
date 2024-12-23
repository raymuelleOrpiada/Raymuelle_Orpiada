class TekkenChar:
    def __init__ (self, name, ability):
        self.name= name
        self.ability=ability
    def Tekken(self, func):
        def wrap_mthd(*args, **kwargs):
            print("Introducing.....")
            func(*args, *kwargs)
            print("This Character is Amazing! ")
        return wrap_mthd
tekks= TekkenChar("Jin","wow kick")
@tekks.Tekken
def emina (char, chara):
    print(f" I am {char} and I can use {chara}")
emina("Jin", "wow kick")