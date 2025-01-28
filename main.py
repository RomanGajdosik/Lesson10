# Intro Object oriented programming
class Person:
    def __init__(self,name,age,gender,occupatiomn):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation =occupatiomn
    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

Roman = Person(name='Roman',age=39,gender='Male',occupatiomn='R.A.E')
Roman.pozdrav()
