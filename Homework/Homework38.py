#  Задание №1
import random
import json

num = [str(i) for i in range(10)]
letter = [chr(i) for i in range(97, 123)]


def let_num():
    all_list = list()
    lst = list()
    for x in range(3):
        if len(all_list) < 2:
            for i in range(10):
                lst.append(random.choice(num))
            all_list.append("".join(lst))
            lst.clear()
        else:
            for i in range(7):
                lst.append(random.choice(letter))
            all_list.append("".join(lst))
            lst.clear()
    return all_list


def update_dict():
    try:
        data = json.load(open("jsdata.json"))
    except FileNotFoundError:
        data = dict()
    res = let_num()

    data[res[1]] = {
        "name": res[2],
        "tel": res[0]
    }
    with open("jsdata.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    update_dict()


# Задание №2 (Необходимо реализовать запись данных о студенте в файл и возможность считывания данных из файла.
# А также запись данных в файл о группе студентов и считывание данных.)


class Student:
    data = dict()

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Студент: {self.name}: {', '.join(map(str, self.marks))}"

    def add_marks(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def st_data_recording(self):
        Student.data[self.name] = self.marks
        with open("data_student.json", "w", encoding='utf-8') as f:
            json.dump(Student.data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def st_data_reading():
        try:
            r = json.load(open("data_student.json"))
            return r
        except:
            raise FileNotFoundError("Файл не найден")


class Group:
    data = dict()

    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = '\n'.join(map(str, self.students))
        return f"Группа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)
        self.sts_data_group_recording()

    def remove_student(self, index):
        s = self.students.pop(index)
        self.sts_data_group_recording()
        return s

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    def sts_data_group_recording(self):
        d = dict()
        for i in range(len(self.students)):
            d[self.students[i].name] = self.students[i].marks
        Group.data[self.group] = d
        with open("data_students_group.json", "w", encoding='utf-8') as f:
            json.dump(Group.data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def st_data_group_reading():
        try:
            r = json.load(open("data_students_group.json"))
            return r
        except:
            raise FileNotFoundError("Файл не найден")


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikalaenka', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
st1.st_data_recording()
st2.st_data_recording()
st3.st_data_recording()
sts = [st1, st2]
my_group = Group(sts, 'ГК Python')
my_group.add_student(st3)
my_group.remove_student(1)
group22 = [st2]
my_group2 = Group(group22, "ГК Web")
Group.change_group(my_group, my_group2, 0)
my_group2.sts_data_group_recording()
my_group.sts_data_group_recording()
print(my_group.st_data_group_reading())
print(st3.st_data_reading())
