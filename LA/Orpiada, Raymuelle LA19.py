class Sinigang:
    def __init__(self, main, texture, taste):
        self.main=main
        self._texture= texture
        self.__taste= taste
    def __str__(self):
        return f" Masarap ang {self.__main} na {self.__texture} medyo maasim at {self.__taste}."

sinigang_yobab= Sinigang("baboy","malapot", "matamis")
sinigang_hipon= Sinigang("hipon", "may butter", "linamnam")
sinigang_vape= Sinigang ("vape", "bagong bili", "nakakasuka")

print(sinigang_yobab)
print(sinigang_hipon)
print(sinigang_vape.__taste)