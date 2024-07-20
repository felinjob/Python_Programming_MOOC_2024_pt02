class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"



def accepted(attempts: list) -> str:
    return list(filter(lambda grade: grade.grade > 0, attempts))

def attempts_with_grade(attempts: list, grade: int) -> str:
    return filter(lambda g: g.grade == grade, attempts)


def passed_students(attempts: list, course: str) -> str:
    course_list = list(filter(lambda c: c.course_name == course, attempts))
    passed = list(filter(lambda g: g.grade > 0, course_list))
    return sorted(map(lambda n: n.student_name, passed))
    

if __name__ == "__main__":
    
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Paula Programmer", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced programming", 3)
    s4 = CourseAttempt("Niles Nerd", "Networking", 3)
    for student in passed_students([s1, s2, s3, s4], "Introduction to Programming"):
        print(student)