class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def __gt__(self, other):
        return self.avg_grade > other.avg_grade

    def calculate_avg_grade(self):
        if not self.grades:
            self.avg_grade = 0
            return

        total_grades = 0
        grades_count = 0

        for course_grades in self.grades.values():
            total_grades += sum(course_grades)
            grades_count += len(course_grades)

        self.avg_grade = round(total_grades / grades_count, 2) if grades_count > 0 else 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.calculate_avg_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    @staticmethod
    def calculate_avg_hw_grade(students_list, course_name):
        total_grades = 0
        grades_count = 0

        for student in students_list:
            if course_name in student.grades:
                course_grades = student.grades[course_name]
                total_grades += sum(course_grades)
                grades_count += len(course_grades)

        if grades_count == 0:
            return 0

        return round(total_grades / grades_count, 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 0

    def calculate_avg_grade(self):
        if not self.grades:
            self.avg_grade = 0
            return

        total_grades = 0
        grades_count = 0

        for course_grades in self.grades.values():
            total_grades += sum(course_grades)
            grades_count += len(course_grades)

        self.avg_grade = round(total_grades / grades_count, 2) if grades_count > 0 else 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def __gt__(self, other):
        return self.avg_grade > other.avg_grade

    @staticmethod
    def calculate_avg_lecture_grade(lecturers_list, course_name):
        total_grades = 0
        grades_count = 0

        for lecturer in lecturers_list:
            if course_name in lecturer.grades:
                course_grades = lecturer.grades[course_name]
                total_grades += sum(course_grades)
                grades_count += len(course_grades)

        if grades_count == 0:
            return 0

        return round(total_grades / grades_count, 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.calculate_avg_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Тестирование
lecturer = Lecturer('Zemlemer', 'K.')
lecturer_1 = Lecturer('Веничка', 'Ерофеев')
reviewer = Reviewer('Josef', 'K.')
reviewer_1 = Reviewer('Вадим', 'Тихонов')
student = Student('Josefine', 'Sangerin', 'Ж')
student_1 = Student('Макс', 'Брод', 'М')

lecturer.courses_attached += ['Python', 'C++']
lecturer_1.courses_attached += ['Python', 'Git']
reviewer.courses_attached += ['Python', 'C++']
reviewer_1.courses_attached += ['Python']
student.finished_courses += ['Введение в программирование']
student.courses_in_progress += ['Python', 'Git']
student_1.courses_in_progress += ['Python', 'C++']

student.rate_lecture(lecturer, 'Python', 9)
student_1.rate_lecture(lecturer, 'Python', 4)
student.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Python', 10)

reviewer.rate_hw(student, 'Python', 1)
reviewer_1.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 2)

students_list = [student, student_1]
lecturers_list = [lecturer, lecturer_1]

print(f"Средняя оценка за домашние задания по Python: {Student.calculate_avg_hw_grade(students_list, 'Python')}")
print(f"Средняя оценка за лекции по Python: {Lecturer.calculate_avg_lecture_grade(lecturers_list, 'Python')}")





