"""
abstraction-it is used to handle the complexity program by hiding the unnecessary infrormation from the user


for abstraction we have to import abc class and abstractionmethod

abc-abstract base class

it is used for hiding the background of the code
"""

from abc import ABC, abstractclassmethod

class RBI(ABC):
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        return 8.5
    
class BOI(RBI):
    def roi(self):
        return 7.5
    

sbi=SBI()
print(sbi.roi())

boi=BOI()
print(boi.roi())