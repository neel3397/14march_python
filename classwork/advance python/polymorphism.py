"""
polymorphism:poly means many morphism means forms.it means many forms.

1.method overloading-python doesnt supports method overloading

2.method overriding-when 2 class have same method name is called method overriding

"""

class animal:
    def walk(self):
        print("animal walking")

class dog:
    def walk(self):
        print("dog walking")


#object creation

r=dog()
r.walk()

r=animal()
r.walk()