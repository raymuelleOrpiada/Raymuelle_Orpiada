from abc import ABC, abstractmethod 

class Pagong(ABC):
    @abstractmethod 
    def langoy(self):
        pass

class Leonardo(Pagong):
    def langoy(self):
        print("Leonardo")

class MichaelAngelo(Pagong):
    def langoy(self):
        print("Michael Angelo")



class Donatello(Pagong):
    def langoy(self):
        print("Donatello")

class Raphael(Pagong):
    def langoy(self):
        print("Raphael")



if __name__ == "__main__":
    
    print ("zoro vs luffy")

    rap= Raphael.langoy= "luffy cant swim"
    print(rap)

    le= Leonardo.langoy= "zoro no way home"
    print(le)

    donz= Donatello.langoy= "usupp wins(???)"
    print(donz)

    usup= MichaelAngelo.langoy= "luffy wins"
    print(usup)