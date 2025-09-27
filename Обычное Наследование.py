class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 9.9

    def __lt__(self, other):  # < (less than)
        return self.avg_grade < other.avg_grade

    def __le__(self, other):  # <= (less or equal)
        return self.avg_grade <= other.avg_grade

    def __eq__(self, other):  # == (equal)
        return self.avg_grade == other.avg_grade

    def __ne__(self, other):  # != (not equal)
        return self.avg_grade != other.avg_grade

    def __gt__(self, other):  # > (greater than)
        return self.avg_grade > other.avg_grade

    def __ge__(self, other):  # >= (greater or equal)
        return self.avg_grade >= other.avg_grade

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.avg_grade}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 9.9

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'

    def __lt__(self, other):  # < (less than)
        return self.avg_grade < other.avg_grade

    def __le__(self, other):  # <= (less or equal)
        return self.avg_grade <= other.avg_grade

    def __eq__(self, other):  # == (equal)
        return self.avg_grade == other.avg_grade

    def __ne__(self, other):  # != (not equal)
        return self.avg_grade != other.avg_grade

    def __gt__(self, other):  # > (greater than)
        return self.avg_grade > other.avg_grade

    def __ge__(self, other):  # >= (greater or equal)
        return self.avg_grade >= other.avg_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

lecturer = Lecturer('Zemlemer', 'K.')
reviewer = Reviewer('Josef', 'K.')
student = Student('Josefine', 'Sangerin', 'Ж')

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
student.finished_courses += ['Введение в программирование']
student.courses_in_progress += ['Python', 'Git']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)

print(student)
print(lecturer)
print(reviewer)

