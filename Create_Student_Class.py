class student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.grades = {"Chinese": 0, "Math": 0, "English": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grade(self):
        print(f"student{self.name} (number:{self.number} )score is:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen = student("小陈", "323232")
chen.set_grade("Chinese", 96)
chen.set_grade("Math", 66)
chen.print_grade()

# def set_score(self, subject, score):
#
#     if subject == 'chinese':
#         self.chinese = score
#     elif subject == 'math':
#         self.math = score
#     elif subject == 'english':
#         self.english = score
#
# def print_score(self):
#
#     print(f'{self.name}的成绩：语文：{self.chinese},数学：{self.math},英语：{self.english}')
