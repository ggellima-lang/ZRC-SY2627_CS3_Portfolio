class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score: float):
        return 0 <= score <= 100

    def __check_submmission(self):
        return len(self.__submitted_files) > 0

    def __is_duplicate(self, file_name: str):
        return file_name in self.__submitted_files

    def add_file(self, file_name: str):
        if self.__is_duplicate(file_name):
            print(f"--> [Warning] '{file_name}' is already attached!")
            return False
        self.__submitted_files.append(file_name)
        self.__is_submitted = True
        print(f"--> [Success] {self.student_name} attached '{file_name}'. Total files: {len(self.__submitted_files)}")
        return True

    def remove_file(self, file_name: str):
        if self.__grade is not None:
            print(f"--> [Warning] {self.student_name} cannot remove files. Assignment already graded.")
            return False

        if file_name in self.__submitted_files:
            self.__submitted_files.remove(file_name)
            if len(self.__submitted_files) == 0:
                self.__is_submitted = False
            print(f"--> [Success] {self.student_name} removed '{file_name}'.")
            return True
        return False

    def assign_grade(self, score: float):
        if not self.__check_submmission():
            print(f"--> [Error] Cannot grade. No files submitted for {self.student_name}.")
            return False

        if self.__validate_grade(score):
            self.__grade = score
            print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")
            return True
        return False

    def get_grade(self):
        return self.__grade if self.__grade is not None else "Not Graded"

    def view_files(self):
        return ", ".join(self.__submitted_files)

    def get_status_report(self):
        status_str = f"Submitted ({len(self.__submitted_files)} files)" if self.__is_submitted else "Missing"
        grade_str = self.get_grade()
        print(f"ID: {self.student_id} | Name: {self.student_name:<16} | Status: {status_str:<20} | Grade: {grade_str}")


# EXECUTION MATCHING EXPECTED OUTPUT

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-101", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
student1.get_status_report()
student2.get_status_report()
student3.get_status_report()
student4.get_status_report()
student5.get_status_report()