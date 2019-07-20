
class Book:

    def __init__(self,id,name,code,publ,price,author):
        self.BookID=id
        self.BookName=name
        self.BookCode=code
        self.BookPubli=publ
        self.BookPrice=price
        self.BookAuthor=author

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


PI=1.02









