
class Marks:
    def __init__(self,phys,chem,math,scien,sports,hist):

        self.MarksPhys=phys
        self.MarksChem=chem
        self.MarksMath=math
        self.MarksScien=scien
        self.MarksSport=sports
        self.MarksHist=hist


    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


