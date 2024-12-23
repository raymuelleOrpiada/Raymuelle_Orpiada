class Sinigang:
    def __init__(self, main, texture, taste):
        self._main=main
        self._texture= texture
        self.__taste= taste
    def __str__(self):
        return f" Masarap ang {self._main} na {self._texture}  medyo maasim at {self.__taste}."
    def di_masarap(self):
        return self.__taste


sinigang_vape= Sinigang ("vape", "bagong bili", "nakakasuka")

print(sinigang_vape.di_masarap())