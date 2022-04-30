from tkinter import *
from tkinter.ttk import *

answers = []

frm = LabelFrame(text="Test 1")
frm.pack()

f = open("Test_1.txt", "r", encoding="UTF-8").readlines()
question = []
answers = []
startq = False
starta = False
for line in f:
    if starta:
        answers.append(line)
    if line == "a:\n":
        startq = False
        starta = True
    if startq:
        question.append(line)
    if line == "q:\n":
        startq = True
answers = list(map(lambda c: c.strip().split("|"), answers))
print(question, answers)

i = 0
count_ans = 0


def Next(e, question, answers, var):
    global i
    global count_ans
    print(i)
    number = var.get()
    if number == int(answers[i-1][3]):
        print("Правильно")
        count_ans += 1
    if i == 5:
        end(e, question)
        return None
    ask_question_block(frm, question, answers, var)


def ask_question_block(frm, question, answers, var=0):
    var = IntVar()
    global i
    ans = answers[i]
    for widget in frm.winfo_children():
        widget.destroy()
    quest = Label(frm, text=question[i]).pack()

    ch1 = Radiobutton(frm, text=ans[0], variable=var, value=1).pack()
    ch2 = Radiobutton(frm, text=ans[1], variable=var, value=2).pack()
    ch3 = Radiobutton(frm, text=ans[2], variable=var, value=3).pack()
    i += 1

    Button(frm, text="Start", command=lambda e=frm: Next(
        e, question, answers, var)).pack()


ask_question_block(frm, question, answers)


def end(frm, question):
    global count_ans
    for widget in frm.winfo_children():
        widget.destroy()
    print(count_ans, int(len(question)))
    print(count_ans/int(len(question)))
    results = "Кол-во правильных: " + str(count_ans) + " из " + str(
        len(question)) + " " + str(count_ans/len(question)*100)[:-2] + "%"
    end_console = Label(frm, text=results).pack()
