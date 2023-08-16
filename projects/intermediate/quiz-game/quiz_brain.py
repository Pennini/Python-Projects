class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_choice, answer):
        if user_choice == answer.lower():
            print("You got it")
            self.score += 1
        else:
            print("It's wrong!")
        print(f"Your current score is {self.score}/{self.question_number}\n")



    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f'Q.{self.question_number}: "{current_question.text}" (True/False)?:').lower()
        while user != "true" and user != "false" and user != "t" and user != "f":
            user = input(f'Q.{self.question_number}: "{current_question}" (True/False)?:').lower()
        if user == "t":
            user = "true"
        else:
            user = "false"
        self.check_answer(user, current_question.answer)



