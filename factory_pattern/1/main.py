from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """interface method
        """

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("im a stundent")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher name"

    def person_method(self):
        print("im a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()

        if person_type == "Teacher":
            return Teacher()

        print('Invalid type')
        return -1


if __name__ == "__main__":
    choice = input("Type of person to create? ")
    person = PersonFactory.build_person(choice)
    person.person_method()
