

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_of_pages)

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def get_number_of_pages(self):
        return self.__number_of_pages

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def get_issue_number(self):
        return self.__issue_number

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)


publication1 = Publication("Introduction to Programming", "John Smith")
publication2 = Publication("Science Today", "Maria Santos")

book1 = Book("Python for Beginners", "Mark Lee", 250)
book2 = Book("The World of Science", "Anna Cruz", 180)

magazine1 = Magazine("National Geographic", "John Doe", 12)
magazine2 = Magazine("Science Monthly", "Emily White", 5)


print("=== PUBLICATIONS ===")
publication1.display_info()
print()
publication2.display_info()

print("\n=== BOOKS ===")
book1.display_info()
print()
book2.display_info()

print("\n=== MAGAZINES ===")
magazine1.display_info()
print()
magazine2.display_info()