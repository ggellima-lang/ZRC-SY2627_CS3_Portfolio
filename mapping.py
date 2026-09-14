class Course:
    def __init__(self, name, instructor, duration):
        self.name = name
        self.instructor = instructor
        self.duration = duration
        self.students = []  

    def add_student(self, student):
        self.students.append(student)

    def display_info(self):
        print(f"Course Name: {self.name}, Instructor: {self.instructor}, Duration: {self.duration} hours")


class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Major: {self.major}")


# Example usage
if __name__ == "__main__":
    course = Course("Python Basics", "Dr. Smith", 40)
    student = Student("Alice", 20, "Computer Science")
    course.add_student(student)
    print(f"Students in {course.name}: {[s.name for s in course.students]}")
