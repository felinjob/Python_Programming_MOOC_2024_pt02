# tee ratkaisusi tänne
class Course:
    def __init__(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__credits = credits
        self.__grade = grade
           
    def course(self):
        return self.__course
    def grade(self):
        return self.__grade
    def credits(self):
        return self.__credits
    
    def switch_grade(self, new_grade):
        self.__grade = new_grade
    
    def __str__(self):
        return f"{self.__course} ({self.__credits} cr) grade {self.__grade}"

class CourseRecords:
    def __init__(self):
        self.__records = {}
        
    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__records:
            self.__records[name] = Course(name, grade, credits)        
        if self.__records[name].grade() < grade:
            self.__records[name].switch_grade(grade)
            
    def course_data(self, course):
        if not course in self.__records:
            return None
        return self.__records[course]
        
    def total_credits(self):
        total_c = 0
        for course in self.__records: 
            total_c += self.__records[course].credits()
        return total_c
    
    def completed_courses(self):
        return len(self.__records)
    
    def grade_list(self):
        grade_list = []
        for course in self.__records:
            grade_list.append(self.__records[course].grade())
        return grade_list
            
    def all_entries(self):
        return self.__records

class Statistics:
    def __init__(self, stats: dict):
        self.__stats = stats
        
    def mean(self):
        grades = self.__stats.grade_list()
        return f"{sum(grades) / len(grades):.1f}"
                
    def grade_distribution(self):
        grades = self.__stats.grade_list()
        index = [1,2,3,4,5]        
        for number in range(len(index), 0, -1):
            print(f"{number}: {grades.count(number) * 'x'}")
    
    def print_stats(self):
        print(f"{self.__stats.completed_courses()} completed courses, a total of {self.__stats.total_credits()} credits")
        print(f"mean {self.mean()}")
        print("grade distribution")
        return self.grade_distribution()
   
class RecordsApp:
    def __init__(self):
        self.__courses = CourseRecords()
        self.__statistics = Statistics(self.__courses)
        
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        
    def add__new_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courses.add_course(course, grade, credits)
        
    def get_course_data(self):
        course = input("course: ")
        data = self.__courses.course_data(course)
        if data == None:
            print("no entry for this course")
        else: 
            print(data)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add__new_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.__statistics.print_stats()
            else: 
                self.help()


teste = RecordsApp()
teste.execute()

