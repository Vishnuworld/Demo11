
class Faculty:

    def __init__(self,id,name,age,sal,exp,gend):

        self.FacultyID=id
        self.FacultyName=name
        self.FacultyAge=age
        self.FacultySal=sal
        self.FacultyExp=exp
        self.FacultyGend=gend


    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)



