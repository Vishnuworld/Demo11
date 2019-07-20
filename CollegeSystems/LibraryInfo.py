
class Library:

    def __init__(self,id,name,staff_no):
        self.LibraryID=id
        self.LibraryName=name
        self.LibraryStaffNo=staff_no


    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

