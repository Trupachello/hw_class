
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in Lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                Lecturer.grades[course] += [grade]
            else:
                Lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if len(self.grades.keys()) == 0:
            return 0
        else:
            sum_grade = sum(sum(grade) for grade in self.grades.values())
            grade_count = sum(len(grade) for grade in self.grades.values())
            return sum_grade / grade_count
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        result += f'Средняя оценка за д/з: {self.average_grade()}\n'
        result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        result += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return 

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        return self.average_grade() == other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if len(self.grades.keys()) == 0:
            return 0
        else:
            sum_grade = sum(sum(grade) for grade in self.grades.values())
            grade_count = sum(len(grade) for grade in self.grades.values())
            return sum_grade / grade_count

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

def students_average_grade(students):
    average_grade = sum(student.average_grade() for student in students) / len(students)
    return average_grade

def lecturers_average_grade(lecturers):
    average_grade = sum(lecturer.average_grade() for lecturer in lecturers) / len(lecturers)
    return average_grade

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')

