class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.grades.values()}
Курсы в процессе изучения: {', '.join([cours for cours in self.courses_in_progress])}
Завершенные курсы: {', '.join([finish_cours for finish_cours in self.finished_courses])}'''

    def lector_rate(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            lector.grade += [grade]
        else:
            return 'Error lector_rate'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grade = []

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {sum(self.grade)/len(self.grade)}'''


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lect = Lecturer('Maiami', 'Ferst')
lect_2 = Lecturer('Farid', 'Anders')

lect.courses_attached += ['django', 'HTML']
lect_2.courses_attached += ['C++', 'git']


best_student.courses_in_progress += ['django']

best_student.lector_rate(lect, 'django', 9)
best_student.lector_rate(lect, 'django', 9)

print(lect.grade)
print(lect_2.grade)

print(best_student)
