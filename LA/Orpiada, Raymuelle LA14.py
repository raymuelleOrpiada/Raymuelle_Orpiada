class Spiderman:
    def __init__(self,name,age):
        self.name=name.upper()
        self.age=age
        
    def describeSpiderman(self):
        print (f" {self.name} is {self.age} years old this year.")

class Tobey(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title=movie_title

class Andrew(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title=movie_title
        
        
class Tom(Spiderman):
    def __init__(self,name,age,movie_title):
        super().__init__(name,age)
        self.movie_title=movie_title
        
spider1=Tobey("tobey maguire" , 49, "spiderman 4")
spider2=Andrew("andrew garfield" , 41, "the returning spiderman")
spider3=Tom("tom holland" , 28, "spider-man: home coming")


print(spider1.name , spider1.movie_title)
print(spider2.name , spider2.movie_title)
print(spider3.name , spider3.movie_title)