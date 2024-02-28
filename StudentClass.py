from datetime import datetime
class Student:

    def __init__(self, sid, n, db, cl ):
        self.__studentID = sid
        self.__name = n
        self.__dob = dob
        self.__classification = cl

    def calc_age(self, dob):
        today = datetime.now().year
        splitdob = dob.split('/')
        current_age = today - splitdob[2]


    def get_current_age(current_age):
        return current_age
    
    def classification(self):
        if self.__classification == 'senior'.lower():
            print('Register 4/1 thru 4/3')
        elif self.__classification == 'junior'.lower():
            print('Register 4/4 thru 4/6')
        elif self.__classification == 'sophomore'.lower():
            print('Register 4/7 thru 4/9')
        elif self.__classification == 'freshman'.lower():
            print('Register 4/10 thru 4/12')
        else:
            print('not valid classisification')

    def get_classification(self):
        return self.__classification


         
        
