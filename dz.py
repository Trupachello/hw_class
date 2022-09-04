
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
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
        if len(self.courses_in_progress) > 1:
            result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        else:
            result += f'Курсы в процессе изучения: {self.courses_in_progress[0]}\n'
        if len(self.finished_courses) > 1:
            result += f'Курсы в процессе изучения: {", ".join(self.finished_courses)}\n'
        elif len(self.finished_courses) < 1:
            result += f'Нет завершенных курсов\n'
        else:
            result += f'Курсы в процессе изучения: {self.finished_courses[0]}\n'
        return result

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
    sum_grade = 0
    grade_count = 0
    for student in students:
        sum_grade += sum(sum(grade) for grade in student.grades.values())
        grade_count += sum(len(grade) for grade in student.grades.values())
    return sum_grade / grade_count


def lecturers_average_grade(lecturers):
    sum_grade = 0
    grade_count = 0
    for lecturer in lecturers:
        sum_grade += sum(sum(grade) for grade in lecturer.grades.values())
        grade_count += sum(len(grade) for grade in lecturer.grades.values())
    return sum_grade / grade_count

def student_test():
    course = 'Python'
    student1 = Student('Gyro', 'Zeppeli', 'man')
    student1.courses_in_progress.append(course)
    print(student1.courses_in_progress)
    student2 = Student('Johny', 'Joestar', 'man')
    student2.courses_in_progress.append(course)

    reviewer = Reviewer('Гриш', 'Ельцов')
    reviewer.add_course(course)

    reviewer.rate_hw(student1, course, 10)
    reviewer.rate_hw(student1, course, 5)
    reviewer.rate_hw(student1, course, 10)

    reviewer.rate_hw(student2, course, 7)

    print(student1)
    print(student1 == student2)
    print(students_average_grade([student1,student2]))


def lecturers_test():
    course = 'Python'

    lecturer_1 = Lecturer('Jotaro', 'Kujo')
    lecturer_1.add_course(course)
    lecturer_2 = Lecturer('Joseph', 'Joestar')
    lecturer_2.add_course(course)

    student_1 = Student('Giorno', 'Giovanna', 'Jojo')
    student_1.courses_in_progress.append(course)
    student_1.rate_Lecturer(lecturer_1, course, 1)
    student_1.rate_Lecturer(lecturer_1, course, 1)
    student_1.rate_Lecturer(lecturer_1, course, 1)
    student_1.rate_Lecturer(lecturer_2, course, 2)

    print(lecturer_1)
    print(lecturer_1.grades)
    print(lecturer_2.average_grade())
    print(lecturer_1.average_grade())
    print(lecturers_average_grade([lecturer_2, lecturer_1]))

student_test()
lecturers_test()

