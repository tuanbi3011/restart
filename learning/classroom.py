from student import Student

class Classroom(Student):

    def __init__(self, name, age, gender, classroom):
        super().__init__(name, age, gender, classroom)
        self.student = []


    def add_student(self, student):
        self.student.append(student)

    def classroom_info(self):
        return f"Sinh viên {self.name}, Tuổi: {self.age}, Giới tính: {self.gender}"

name1 = Classroom("Bucky", 20, "nam","CNTT" )
print(name1.classroom_info())

def main():
    classroom = Classroom("Lớp 304", None, None, "304")
    print(f"Classroom info: {classroom.classroom_info()}")

    name3 = Student("Alice", 12, "nữ", "CNTT")
    name4 = Student("Bob", 13, "nam", "CNTT")


    classroom.add_student(name3)
    classroom.add_student(name4)

    print(classroom.classroom_info())

    for student in classroom.student:
        print(f"{student.name}")

if __name__ == "__main__":
    main()
pass


