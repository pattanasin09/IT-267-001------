from student import Student
class Itds(Student):
    def __init__(self, stuid, name, major) -> None:
        super().__init__(stuid, name, major)

    def display_NameAndMajor(self):
        print(f'ITDS Name : {self._name}')
        return super().display_NameAndMajor()