from data import question_data
from question_model import Question
import random
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q_text = item['question']
    q_answer = item['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've finished the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")