                        #1. Import all the files from directory

from CollegeSystems.BookInfo import Book
from CollegeSystems.CollegeInfo import College
from CollegeSystems.DeptInfo import Department
from CollegeSystems.FacultyInfo import Faculty
from CollegeSystems.LibraryInfo import Library
from CollegeSystems.MarksInfo import Marks
from CollegeSystems.StudentsInfo import Student


CSEDept=Department(id=111,name='Computer',code='CSE')
MECHDept=Department(id=222,name='Mechanical',code='MECH')
CVLDept=Department(id=333,name='Civil',code='CVL')
ITDept=Department(id=444,name='Info Tech',code='IT')
EEEDept=Department(id=555,name='Electrcal',code='EEE')

#print('Departments created successfully')

ST1=Student(id=10,name='Vishnu',age=24,gender='Male',bloodg='B+',status='Single')
ST2=Student(id=20,name='Vaishnavi',age=20,gender='Female',bloodg='B+',status='Single')
ST3=Student(id=30,name='Vinayak',age=24,gender='Male',bloodg='B-',status='Engaged')
ST4=Student(id=40,name='Mayuri',age=26,gender='Female',bloodg='A+',status='Single')
ST5=Student(id=50,name='Vaidehi',age=22,gender='Female',bloodg='AB+',status='Engaged')
ST6=Student(id=60,name='Sushmita',age=23,gender='Female',bloodg='O-',status='Single')


#print('Students created successfully')

F1=Faculty(id=100,name='Karuna',age=34,sal=30000,exp=5,gend='Female')
F2=Faculty(id=101,name='Singh',age=23,sal=18000,exp=5,gend='Male')
F3=Faculty(id=102,name='Sharma',age=51,sal=50000,exp=5,gend='Female')
F4=Faculty(id=103,name='Bhandari',age=21,sal=60000,exp=5,gend='Male')
F5=Faculty(id=104,name='Kadtan',age=29,sal=20000,exp=5,gend='Male')
F6=Faculty(id=105,name='Jadhav',age=32,sal=65000,exp=5,gend='Male')
F7=Faculty(id=106,name='Ketaki',age=22,sal=38000,exp=5,gend='Female')



#print('Faculties created successfully')

Book1=Book(id=999,name='Python',code=501,publ='AAA',price=500,author='BBB')
Book2=Book(id=888,name='C',code=502,publ='CCC',price=230,author='DDD')
Book3=Book(id=777,name='CPP',code=503,publ='EEE',price=450,author='FFF')
Book4=Book(id=666,name='Selenium',code=504,publ='GGG',price=300,author='HHH')
Book5=Book(id=555,name='Testing',code=505,publ='III',price=250,author='JJJ')
Book6=Book(id=444,name='JAVA',code=506,publ='KKK',price=560,author='LLL')



#print('Books created successfully')

Mark1=Marks(phys=74,chem=54,math=76,scien=64,sports=98,hist=42)
Mark2=Marks(phys=18,chem=42,math=41,scien=36,sports=48,hist=12)
Mark3=Marks(phys=44,chem=69,math=61,scien=61,sports=65,hist=51)
Mark4=Marks(phys=24,chem=97,math=65,scien=66,sports=94,hist=54)
Mark5=Marks(phys=39,chem=40,math=40,scien=40,sports=26,hist=14)
Mark6=Marks(phys=0,chem=0,math=0,scien=0,sports=0,hist=0)

# print('Marks created successfully')

                        #4. Allot marks  to each student.
ST1.Marks=Mark1
ST2.Marks=Mark2
ST3.Marks=Mark3
ST4.Marks=Mark4
ST5.Marks=Mark5
ST6.Marks=Mark6
                        #5. Allot Dept  to each student.
ST1.Dept=CSEDept
ST2.Dept=CVLDept
ST3.Dept=MECHDept
ST4.Dept=ITDept
ST5.Dept=CSEDept
ST6.Dept=EEEDept
                        #6. Allot Books to each student.
#print(ST1.Marks)
ST1.Books=[Book1,Book3,Book5]
ST2.Books=[Book1,Book5]
ST3.Books=[Book4,Book3]
ST4.Books=[Book6,Book1]
ST5.Books=[Book4,Book2]
ST6.Books=[Book5,Book3]



library=Library(id=789,name='Central',staff_no=6)

                    #4. Create list of books
library.listofbooks=[Book1,Book2,Book3,Book4,Book5,Book6,Book4,Book6,Book3,Book5,Book1,Book2,Book3,Book2,Book5,Book4]
#print(len(library.listofbooks))


#print('Library created successfully')

college=College(id=123456,name='Alard',addr='Pune')

#print('College created successfully')

                        # 3. Create a list of all the objects which is present in college.

CollegeDept={CSEDept,CVLDept,EEEDept,ITDept,MECHDept}
CollegeFaculty=[F1,F2,F3,F4,F5,F6,F7]
CollgeStudent={ST1,ST2,ST3,ST4,ST5,ST6}
CollgeLibrary=library

'''
for item in CollegeFaculty:
      if item.FacultySal>=30000:
        print('The salary of',item.FacultyName,'is',item.FacultySal,'.')
      else: print(item.FacultyName,'has lower salary.')



op= 
The salary of Karuna is 30000 .
Singh has lower salary.
The salary of Sharma is 50000 .
The salary of Bhandari is 60000 .
Kadtan has lower salary.
Jadhav has lower salary.
The salary of Ketaki is 38000 .

'''



#print(CollegeDept)
#print(CollegeFaculty)
#print(CollgeStudent)   # Records of all the stuffs.
#print(CollgeLibrary)


#for i in CollgeStudent:
 #   print(i)            # prints all the details of all the students.


# Sorting_Started

#print(len(CollegeDept))    # No of dept in college = 5
#print(len(CollegeFaculty))  # No of faculty in college = 7
#print(len(CollgeStudent))   # No of student in college = 6



# Get the names of students who has >price valued books with price of book.

def getbookpricewithname(price):
    for stud in CollgeStudent: # list madhle students
        for book in stud.Books:
                if book.BookPrice>=price:
                    print(stud.StudName , "has book with price",book.BookPrice,'.')

#getbookpricewithname(500)

'''

def getstudWiseAgrt():
    for stud in CollgeStudent:
        stagr = round((stud.Marks.MarksPhys+stud.Marks.MarksMath+stud.Marks.MarksChem)/3,2)
        print(stud.StudName +" Aggrt marks" , stagr)
        stud.stagr=stagr
getstudWiseAgrt()


'''




Total=0
for index,item in enumerate(CollegeFaculty):
   # for i in range(len(CollegeFaculty)):
    Total+=item.FacultySal
   # print(index,item.FacultySal)
#print(Total)



Total=0
for index,item in enumerate(CollegeFaculty):
    Total+=item.FacultySal
   # print(index,item.FacultySal)



#Inreament salary by 20% if faculti's age is  more than 25 and having less salary  than 25000.
def faculty_increament(sal,age):
    for item in CollegeFaculty:
        #print(item.FacultySal)
        if item.FacultySal<sal and item.FacultyAge>age:
#print(item.FacultyName,item.FacultyAge,item.FacultySal)
            item.FacultySal=round(item.FacultySal+(0.20*item.FacultySal))
        print(item.FacultySal)

    print(CollegeFaculty)

faculty_increament(50000,25)


'''
faculty_increament(50000,25)

for item in CollgeStudent:
    Std=round((item.Marks.MarksChem+item.Marks.MarksMath+item.Marks.MarksPhys+item.Marks.MarksHist+item.Marks.MarksScien+item.Marks.MarksSport)/6,2)
    #print(item.StudName,Std)



    if Std>40:
        print(item.StudName,'is passed.')

    else:
        #print(item.StudName,'is failed.')


        print(item.StudName,'is failed.')

'''



#Subject_List=['MarksSport','MarksScien','MarksHist',"MarksPhys","MarksMath","MarksChem"]


#if Mark1.MarksPhys>40 and Mark1.MarksChem>40 and Mark1.MarksMath>40 and Mark1.MarksHist>40 and  Mark1.MarksScien>40:
#   print('Passed')
#else:
#   print('Failed')
'''
count=1
for i in Mark1:
    if Mark1.i:
        count=count and 1
    else:
        count = count and 0
if count==1:
    print("passed")
else:
    print("failed")
'''

for i in CollgeStudent:
    print(i.Marks)




