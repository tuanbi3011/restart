class Student:
    def __init__(self, name, age, gender, classroom):
        self.name = name
        self.age = age
        self.gender = gender
        self.classroom = classroom

    def __str__(self):
        return f"Student {self.name}, Age: {self.age}, Gender: {self.gender}, Classroom: {self.classroom}"

    def __introduce__(self):
        return f"{self.name} hiện tại {self.age} years old, là {self.gender}, học lớp {self.classroom}"

name1 = Student("Bucky", 20, "nam", "CNTT")
name2 = Student("Aurora", 25, "nữ", "Ngôn Ngữ Anh")
print(name1.__introduce__())
print(name2.__introduce__())

