import StudentClass as sc 

def main():

    student = sc.Student('8911155', 'John', '02/28/1999', 'junior')

    print('age:', student.get_student_age())

    print(student.get_registration())

main()