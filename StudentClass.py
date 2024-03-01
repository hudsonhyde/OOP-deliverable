from datetime import datetime
class Student:

    def __init__(self, sid, n, dob, cl ):
        self.__studentID = sid
        self.__name = n
        self.__dob = dob
        self.__classification = cl
        self.__age = 0

    def calc_student_age(self):
        today = datetime.now().year
        splitdob = self.__dob.split('/')
        year = int(splitdob[2])
        age = today - year
        return age

    
    def registration(self):
        if self.__classification == 'senior':
            return 'Register 4/1 thru 4/3'
        elif self.__classification == 'junior':
            return 'Register 4/4 thru 4/6'
        elif self.__classification == 'sophomore':
            return 'Register 4/7 thru 4/9'
        elif self.__classification == 'freshman':
            return 'Register 4/10 thru 4/12'
        else:
            return 'Not valid classification'

    def get_registration(self):
        return self.registration()
    
    def get_student_age(self):
        return self.calc_student_age()


         
        
