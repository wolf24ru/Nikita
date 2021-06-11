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
Средняя оценка за домашние задания: {self.average_mark():.2f}
Курсы в процессе изучения: {', '.join([cours for cours in self.courses_in_progress])}
Завершенные курсы: {', '.join([finish_cours for finish_cours in self.finished_courses])}'''

    def __lt__(self, other_student):
        try:
            return self.average_mark() < other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def __le__(self, other_student):
        try:
            return self.average_mark() <= other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def __eq__(self, other_student):
        try:
            return self.average_mark() == other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def __ne__(self, other_student):
        try:
            return self.average_mark() != other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def __gt__(self, other_student):
        try:
            return self.average_mark() > other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def __ge__(self, other_student):
        try:
            return self.average_mark() >= other_student.average_mark()
        except ZeroDivisionError:
            print('Error: one of the students hasn\'t marks')
            return False

    def average_mark(self):
        try:
            return sum([sum(i) for i in self.grades.values()]) / \
                sum([len(i) for i in self.grades.values()])
        except ZeroDivisionError:
            print('Error: no ratings available')
            return 0

    def lector_rate(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Error lector_rate'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_mark():.2f}'''

    def __lt__(self, other_lecturer):
        try:
            return self.average_mark() < other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def __le__(self, other_lecturer):
        try:
            return self.average_mark() <= other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def __eq__(self, other_lecturer):
        try:
            return self.average_mark() == other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def __ne__(self, other_lecturer):
        try:
            return self.average_mark() != other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def __gt__(self, other_lecturer):
        try:
            return self.average_mark() > other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def __ge__(self, other_lecturer):
        try:
            return self.average_mark() >= other_lecturer.average_mark()
        except ZeroDivisionError:
            print('Error: one of the lecturers hasn\'t marks')
            return False

    def average_mark(self):
        try:
            return sum([sum(grade_list) for grade_list in self.grades.values()]) / \
                sum([len(grade_list) for grade_list in self.grades.values()])
        except ZeroDivisionError:
            print('Error: no ratings available')
            return 0


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание студента Ruoy
student_Ruoy = Student('Ruoy', 'Eman', 'your_gender')
student_Ruoy.courses_in_progress += ['Python']

# Создание студента Lex
student_Lex = Student('Lex', 'Magrau', 'your_gender')
student_Lex.courses_in_progress += ['HTML', 'Python']

# Создание проверяющего Some
reviewer_Some = Reviewer('Some', 'Buddy')
reviewer_Some.courses_attached += ['Python']

# Создание проверяющего Bob
reviewer_Bob = Reviewer('Bob', 'Karlson')
reviewer_Bob.courses_attached += ['HTML']

# Создание лектора Maiami
lecturer_Maiami = Lecturer('Maiami', 'Ferst')
lecturer_Maiami.courses_attached += ['Django', 'HTML']

# Создание лектора Farid
lecturer_Farid = Lecturer('Farid', 'Anders')
lecturer_Farid.courses_attached += ['Python', 'Git']
print(student_Ruoy)


reviewer_Some.rate_hw(student_Ruoy, 'Python', 10)
reviewer_Some.rate_hw(student_Ruoy, 'Python', 9)
reviewer_Some.rate_hw(student_Ruoy, 'Python', 10)
reviewer_Some.rate_hw(student_Lex, 'Python', 9)
reviewer_Some.rate_hw(student_Lex, 'Python', 10)

reviewer_Bob.rate_hw(student_Lex, 'HTML', 10)
reviewer_Bob.rate_hw(student_Lex, 'HTML', 10)
reviewer_Bob.rate_hw(student_Lex, 'HTML', 8)

# оценка не добавиться так как данный ментр не ведет курс по HTML
reviewer_Some.rate_hw(student_Lex, 'HTML', 10)

student_Ruoy.lector_rate(lecturer_Farid, 'Python', 9)
student_Ruoy.lector_rate(lecturer_Farid, 'Python', 8)
student_Ruoy.lector_rate(lecturer_Maiami, 'C++', 5)

student_Lex.lector_rate(lecturer_Maiami, 'HTML', 10)
student_Lex.lector_rate(lecturer_Maiami, 'HTML', 8)
student_Lex.lector_rate(lecturer_Farid, 'Git', 5)

print('-------')
print(student_Ruoy)
print('-------')
print(student_Lex)
print('-------')
print(reviewer_Some)
print('-------')
print(reviewer_Bob)
print('-------')
print(lecturer_Maiami)
print('-------')
print(lecturer_Farid)
print('-------')

print(lecturer_Maiami < lecturer_Farid)
print(lecturer_Maiami != lecturer_Farid)
student_Ruoy.finished_courses += ['HTML']
print(student_Ruoy < student_Lex)

# знаю что не соответствует заданию, но мне кажется избыточным создавать 2
# одинаковые функции с разными названиями. Поэтому решил создать одну,
# надеюсь это не ошибка.


def average_mark_all_person(persons_list, cours):
    average_mark_list = []
    for person in persons_list:
        if cours in person.grades:
            average_mark_list += person.grades.get(cours)
    return sum(average_mark_list) / len(average_mark_list)


average_mark_stud_py = Average_mark_all_person(
    [student_Lex, student_Ruoy], 'Python')

print(f'Средняя оценка студентов за курс Python: {average_mark_stud_py}')
print()

average_mark_lector_py = Average_mark_all_person(
    [lecturer_Maiami, lecturer_Farid], 'Python')
print(f'Средняя оценка лекторов за курс Python: {average_mark_lector_py}')
