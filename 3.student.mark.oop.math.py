import math
import numpy as np
import curses

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
        self.credits = {}

    def add_mark(self, course, mark, credit):
        self.marks[course] = math.floor(mark)
        self.credits[course] = credit

    def get_mark(self, course):
        return self.marks.get(course, 0)

    def calculate_GPA(self):
        marks = np.array(list(self.marks.values()))
        credits = np.array(list(self.credits.values()))
        return np.average(marks, weights=credits)

    def display(self):
        return f"ID: {self.id}, Name: {self.name}, GPA: {self.calculate_GPA()}"

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

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
        students_sorted = sorted(self.students, key=lambda student: student.calculate_GPA(), reverse=True)
        for student in students_sorted:
            print(student.display())

    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}, Credit: {course.credit}")

    def list_marks(self):
        for student in self.students:
            for course, mark in student.marks.items():
                print(f"Student ID: {student.id}, Course ID: {course.course_id}, Mark: {mark}, Credit: {student.credits[course]}")

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

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
            credit = int(input("Credit of the course: "))
            course = Course(course_id, name, credit)
            school.add_course(course)
        elif option == 3:
            student_id = input("Student ID: ")
            course_id = input("Course ID: ")
            mark = float(input("Mark: "))
            student = school.get_student(student_id)
            course = school.get_course(course_id)
            if student and course:
                student.add_mark(course, mark, course.credit)
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

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

if __name__ == "__main__":
    main()
