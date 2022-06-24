import random


def get_question():
    with open('questions.txt', 'r') as f:
        question_list = f.read().splitlines()

    number_question = random.randrange(0, len(question_list))
    question_answer = str(question_list[number_question])

    for i in range(0, len(question_answer)):
        if question_answer[i] == ';':
            question = question_answer[0:i]
            answer = question_answer[i+1:len(question_answer)]
    return answer, question


answer, question = get_question()
print('Программа чувствительна к регистру! Вы можете ввести либо полностью всё слово, либо лишь одну букву!')
print(question)
current_view = []
for i in range (0, len(answer)):
    current_view.append('*')

print(''.join(current_view))

while True:
    user = input('Введите букву или назовите слово: ')
    user_answer = ''
    if user == answer:
        print('Вы правильного угадали слово!')
        break

    if user in answer:
        print('Такая буква есть!')
        for i in range (0, len(answer)):
            if answer[i] == user:
                current_view[i] = user
                user_answer = ''.join(current_view)
    else:
        print('Такой буквы нет!')

    if user_answer == answer:
        print('Вы правильно назвали все буквы!')
        break

    print(user_answer)