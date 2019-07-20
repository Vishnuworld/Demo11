
class Department:

    def __init__(self,id,name,code):

        self.DeptID=id
        self.DeptName=name
        self.DeptCodde=code


    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


