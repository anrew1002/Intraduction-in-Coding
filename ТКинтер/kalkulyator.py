import tkinter as tk


def func():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        label.config(text="Сумма чисел будет равна {}".format(x + y))
    except ValueError:
        label.config(text="Ошибка, введите цифры")


root = tk.Tk()
entry_1 = tk.Entry(root, )
entry_2 = tk.Entry(root)
#frame=tk.Frame(root, padding=10)
#frame.pack()
entry_1.pack()
entry_2.pack()
label = tk.Label(root, text="Введите числа", height=3)
label.pack()
button = tk.Button(root, text='сложить числа', command=func,width=70)
button.pack()
root.mainloop()
