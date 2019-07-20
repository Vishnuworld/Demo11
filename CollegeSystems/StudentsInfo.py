
class Student:

    def __init__(self,id,name,age,gender,bloodg,status):
        self.StudID=id
        self.StudName=name
        self.StudAge=age
        self.StudGender=gender
        self.StudBloodG=bloodg
        self.StudentStatus=status



    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)



