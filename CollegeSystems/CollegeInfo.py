
class College:

    def __init__(self,id,name,addr):

        self.collegID=id
        self.collegName=name
        self.collegAddre=addr

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)



