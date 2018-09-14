# Create your classes here

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print(self.question) 
        answer = input("Answer: ")   

        return answer == self.answer

class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question) 

    def administer(self):
        counter = 0
        score = 0

        for question in self.questions:
            is_correct = question.ask_and_evaluate()
            counter += 1
            if is_correct:
                score += 1

        print("Your score is {}".format(100 * score / counter))
        return (100 * score / counter)        
        # print("Your score is {}".format(100 * score / len(self.questions)))


class StudentExam:
    score = float()

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam


    def take_test(self):
        self.score = self.exam.administer()


def example():
    midterm = Exam("midterm")
    question1 = Question("What color is the sky?", "Blue")
    question2 = Question("Whats your favorite coding language?", "Python")
    midterm.add_question(question1)
    midterm.add_question(question2)
    jane = Student("Jane", "Pain", "123 street")
    jane_exam = StudentExam(jane, midterm)
    jane_exam.take_test()

