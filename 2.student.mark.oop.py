class Person:
    def __init__(self, id, name, date_of_birth):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
    def display(self):
        raise NotImplementedError("Subclass must implement this method")
class Student(Person):
    def __init__(self, student_id, name, date_of_birth):
        super().__init__(student_id, name, date_of_birth)
        self.marks = {}
    def add_mark(self, course, mark):
        self.marks[course] = mark
    def get_mark(self, course):
        return self.marks.get(course, 0)
    def display(self):
        return f"ID: {self.id}, Name: {self.name}"
class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
class School:
    def __init__(self):
        self.students = []
        self.courses = []
    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Invalid student")
        self.students.append(student)
    def add_course(self, course):
        self.courses.append(course)
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None
    def list_students(self):
        for student in self.students:
            print(student.display())
    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")
    def list_marks(self):
        for student in self.students:
            for course, mark in student.marks.items():
                print(f"Student ID: {student.id}, Course ID: {course.course_id}, Mark: {mark}")
def main():
    school = School()
    while True:
        print("1. Input student info")
        print("2. Input course info")
        print("3. Input mark")
        print("4. List students")
        print("5. List courses")
        print("6. List marks")
        print("7. Exit")
        option = int(input("Select an option: "))
        if option == 1:
            student_id = input("Student ID: ")
            name = input("Name: ")
            date_of_birth = input("Date of birth (example: dd/mm/yyyy): ")
            student = Student(student_id, name, date_of_birth)
            school.add_student(student)
        elif option == 2:
            course_id = input("Course ID: ")
            name = input("Name of the course: ")
            course = Course(course_id, name)
            school.add_course(course)
        elif option == 3:
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            mark = float(input("Mark: "))
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark)
        elif option == 4:
            school.list_students()
        elif option == 5:
            school.list_courses()
        elif option == 6:
            school.list_marks()
        elif option == 7:
            break
        else:
            print("No option valid. Try again")
if __name__ == "__main__":
    main()
