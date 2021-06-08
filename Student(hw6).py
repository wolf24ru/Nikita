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
Средняя оценка за домашние задания: {self.average_mark()}
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
        return sum([sum(i) for i in self.grades.values()]) / \
            sum([len(i) for i in self.grades.values()])

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
        super().__init__(name, surname)
        self.grade = []

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_mark()}'''

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
        return sum(self.grade) / len(self.grade)


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


student_Ruoy = Student('Ruoy', 'Eman', 'your_gender')
student_Ruoy.courses_in_progress += ['Python']

student_Lex = Student('Lex', 'Magrau', 'your_gender')
student_Lex.courses_in_progress += ['HTML']

mentor_Some = Reviewer('Some', 'Buddy')
mentor_Some.courses_attached += ['Python']

mentor_Bob = Reviewer('Bob', 'Karlson')
mentor_Bob.courses_attached += ['HTML']

lecturer_Maiami = Lecturer('Maiami', 'Ferst')
lecturer_Maiami.courses_attached += ['Django', 'HTML']

lecturer_Farid = Lecturer('Farid', 'Anders')
lecturer_Farid.courses_attached += ['Python', 'Git']


mentor_Some.rate_hw(student_Ruoy, 'Python', 10)
mentor_Some.rate_hw(student_Ruoy, 'Python', 9)
mentor_Some.rate_hw(student_Ruoy, 'Python', 10)

mentor_Bob.rate_hw(student_Lex, 'HTML', 10)
mentor_Bob.rate_hw(student_Lex, 'HTML', 10)
mentor_Bob.rate_hw(student_Lex, 'HTML', 8)

# оценка не добавиться так как данный ментр не ведет курс по HTML
mentor_Some.rate_hw(student_Lex, 'HTML', 10)

student_Ruoy.lector_rate(lecturer_Farid, 'Python', 9)
student_Ruoy.lector_rate(lecturer_Farid, 'Python', 8)
student_Ruoy.lector_rate(lecturer_Maiami, 'C++', 5)

student_Lex.lector_rate(lecturer_Maiami, 'HTML', 10)
student_Lex.lector_rate(lecturer_Maiami, 'HTML', 8)
student_Lex.lector_rate(lecturer_Farid, 'Git', 5)

print('-------')
print(student_Ruoy)
print('-------')

student_Ruoy.finished_courses += ['HTML']

print(student_Ruoy < student_Lex)
