import random
from random import *
from tkinter import *
from tkinter import messagebox

# firstly, we need to create the list with answers
# answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
# 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
# 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
# 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
# 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
#
# # hello = input('Enter your name: ') # secondly, we ask a user to enter his/her name
# # print(f"Hi, {hello}, I'm a magic ball, and I know the answer to any question you have.") # then we
#
# def magic_ball():
#     again = 'q'
#     while again.lower() != 'q':
#         question = input('Ask your question: ')
#         print(choice(answers))
#         again = input('One more question? (Enter "q", if you wish to stop, '
#                       'to continue enter any word or symbol): ')
#
#         if again.lower() == 'q':
#             print('Come back if you have any questions!')

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений',
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да',
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

# hello = input('Enter your name: ') # secondly, we ask a user to enter his/her name
# print(f"Hi, {hello}, I'm a magic ball, and I know the answer to any question you have.") # then we

def magic_ball():
    question = question_tf.get()
    messagebox.showinfo('Ответ', choice(answers))

window = Tk()
window.title("Magic ball")
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

question_lb = Label(
    frame,
    text="Введите свой вопрос:  "
)
question_lb.grid(row=3, column=1)

question_tf = Entry(
   frame,
)
question_tf.grid(row=3, column=2, pady=5)

answ_btn = Button(
   frame,
   text='Получить ответ',
   command=magic_ball
)
answ_btn.grid(row=5, column=2)


window.mainloop()