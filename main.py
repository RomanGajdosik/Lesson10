# Intro Object oriented programming
class Person:
    def __init__(self,name,age,gender,occupatiomn):
        self.__name = name # private
        self.age = age
        self.gender = gender
        self.occupation =occupatiomn
    def pozdrav(self):
        print(f"Ahoj volam sa {self.__name} a mam {self.age} rokov")

Roman = Person(name='Roman',age=39,gender='Male',occupatiomn='R.A.E')

#Roman.age =50
print(Roman.age)
