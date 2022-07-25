class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        # self.questions_list = input(f"Q.{self.question_number + 1}: {question_bank[0].text} (True/False)?: ").lower()
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number }: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("That's right!")
        else:
            print("That's incorrect")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")


