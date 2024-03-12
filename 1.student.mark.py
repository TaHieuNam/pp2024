student = []
courses = []
marks = []

#input student in4
def input_student_in4():
    student_name = input("Name: ")
    student_id = input("Student ID: ")    
    student_date_of_birth = input("Date of birth (example: dd/mm/yyyy) : ")
    student.append((student_id,student_name,student_date_of_birth))

#input course in4
def input_course_in4():
    course_name = input("Name of the course: ")
    course_id = input("course ID: ")
    course.append((course_name,course_id))
    
#input marks
def input_marks():
    student_id = input("Student ID: ")   
    course_id = input("course ID: ") 
    mark = float(input("Mark: "))
    student.append((student_id,course_id, mark))
    
#list course
def list_course():
    for course in courses:
        print(f"ID:{course[0]}, Name:{course[1]}")
        
#list marks
def list_mark():
    for mark in marks:
        print(f"student ID:{mark[0]}, course ID:{mark[1]}, mark: {mark[2]}")

#main funct to drive prog
def main():
    while True:
        print("1.input student info")
        print("2.input course info")
        print("3.input mark")
        print("4.list students")
        print("5.list courses")
        print("6.list marks")
        print("7.exit")
        option = int(input("Select an option: "))
        if option == 1:
            input_student_in4()
        elif option == 2:
            input_course_in4()
        elif option == 3:
            input_marks()
        elif option == 4:
            list_students()
        elif option == 5:
            list_courses()
        elif option == 6:
            list_marks()
        elif option == 7:
            break
        else:
            print("No option valid. Try again")

#run main funct
if __name__ == "__main__":
    main()
            
        
        