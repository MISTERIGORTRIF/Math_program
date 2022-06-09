from tkinter import *
from tkinter import messagebox
import math

def instruction():
    window = Tk()

    window.eval('tk::PlaceWindow . center')

    window.title('Инструкция')
    window.geometry('600x200')
    window.resizable(False, False)

    label_instr1 = Label(window, text='1. Введите число в поле ввода.')
    label_instr1.grid(row=0, column=0, sticky='w')

    label_instr2 = Label(window, text='2. Нажмите <Рассчитать!>.')
    label_instr2.grid(row=1, column=0, sticky='w')

    label_instr3 = Label(window, text='3. Программа работает только с целыми числами и не поддерживает команды из библиотеки <math>.')
    label_instr3.grid(row=2, column=0, sticky='w')

    label_instr4 = Label(window, text='Сделано с любовью в пылающей печи подземного царства.')
    label_instr4.grid(row=3, column=0, sticky='w')

    label_instr5 = Label(window, text='MISTERIGORTRIF©')
    label_instr5.grid(row=4, column=0)


    window.mainloop()

def pravka(s):
    return s.replace('.','',1).isdigit()

def priloga():
  global ploshad
  global perimetr
  global R
  global r
  global angle1
  global angle2
  global angle3
  global k
  arr = []
  a1 = a_entry.get()
  a2 = b_entry.get()
  a3 = c_entry.get()
  if pravka(a1) and pravka(a2) and pravka(a3):
    arr = []
    a = int(a_entry.get())
    b = int(b_entry.get())
    c = int(c_entry.get())
    for i in range(1):
        arr.append(a)
        arr.append(b)  # Записываем в массив для удобства
        arr.append(c)
    nice = max(arr)
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):  # Пузырьковая сортировка
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    sum = arr[0] + arr[1]
    if nice >= sum:
        messagebox.showinfo('Ошибка!', 'Такого треугольника не существует!')
    else:
        x = ((arr[0]) ** 2 + (arr[1]) ** 2 - (nice) ** 2) / (2 * (arr[0]) * (arr[1]))  # Вид треугольника
        if a == b == c:
            k = 'Равносторонний'
        else:
            if a == b or a == c or b == c:
                k = 'Равнобедренный'
            else:
                if x > 0:
                    k = 'Остроугольный'
                if x < 0:
                    k = 'Тупоугольный'
                if x == 0:
                    k = 'Прямоугольный'
        angle1 = (math.acos(x) * 180) / (3.14)
        m = (arr[0] ** 2 + (nice) ** 2 - arr[1] ** 2) / (2 * arr[0] * nice)
        angle2 = (math.acos(m) * 180 / (3.14))  # Нахождение углов
        angle3 = 180 - (angle1 + angle2)
        perimetr = a + b + c  # Периметр
        pp = 0.5 * (a + b + c)  # Полупериметр
        ploshad = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))  # Площадь
        R = (a * b * c) / (4 * ploshad)  # Радиус описанной окружности
        r = ploshad / pp  # Радиус вписанной окружности
        r = round(r, 2)
        R = round(R, 2)
        angle1 = round(angle1)
        angle2 = round(angle2)
        angle3 = round(angle3)

        win = Tk()
        win.title('Решения треугольника')
        win.minsize(300, 200)
        win.resizable(height=True, width=True)

        vid_label = Label(win, text='Вид треугольника:')
        vid_label.grid(row=1, column=1, sticky='w')
        vid_label1 = Label(win, text=k)
        vid_label1.grid(row=1, column=2)

        ploshad_label = Label(win, text='Площадь треугольника:')
        ploshad_label.grid(row=2, column=1, sticky='w')
        ploshad_label1 = Label(win, text=ploshad)
        ploshad_label1.grid(row=2, column=2)

        perimetr_label = Label(win, text='Периметр треугольника:')
        perimetr_label.grid(row=3,column=1, sticky='w')
        perimetr_label1 = Label(win, text=perimetr)
        perimetr_label1.grid(row=3, column=2)

        radius_op_label = Label(win, text='Радиус описанной окружности:')
        radius_op_label.grid(row=4,column=1, sticky='w')
        radius_op_label1 = Label(win, text=R)
        radius_op_label1.grid(row=4, column=2)

        radius_vp = Label(win, text='Радиус вписанной окружности:')
        radius_vp.grid(row=5, column=1)
        radius_vp1 = Label(win, text=r)
        radius_vp1.grid(row=5, column=2)

        angle1_label = Label(win, text='Угол №1:'+' '+'(В градусах)')
        angle1_label.grid(row=6, column=1, sticky='w')
        angle11_label = Label(win, text=angle1)
        angle11_label.grid(row=6, column=2)

        angle2_label = Label(win, text='Угол №2:'+' '+'(В градусах)')
        angle2_label.grid(row=7, column=1, sticky='w')
        angle22_label = Label(win, text=angle2)
        angle22_label.grid(row=7, column=2)

        angle3_label = Label(win, text='Угол №3:'+' '+'(В градусах)')
        angle3_label.grid(row=8, column=1, sticky='w')
        angle33_label = Label(win, text=angle3)
        angle33_label.grid(row=8, column=2)

        win.eval('tk::PlaceWindow . center')

        win.resizable(False, False)

        win.mainloop()
  else:
      messagebox.showinfo('Ошибка!', 'Введите число!')

root = Tk()
root.title("Решения треугольника")

a = StringVar()
b = StringVar()
c = StringVar()

a_label = Label(text="Введите первую сторону треугольника:")
b_label = Label(text="Введите вторую сторону треугольника:")
c_label = Label(text='Введите третью сторону треугольника:')

a_label.grid(row=0, column=0, sticky="w")
b_label.grid(row=1, column=0, sticky="w")
c_label.grid(row=2, column=0, sticky='w')

a_entry = Entry(textvariable=a)
b_entry = Entry(textvariable=b)
c_entry = Entry(textvariable=c)

a_entry.grid(row=0, column=1, padx=5, pady=5)
b_entry.grid(row=1, column=1, padx=5, pady=5)
c_entry.grid(row=2, column=1, padx=5, pady=5)

message_button = Button(text="Рассчитать!", command=priloga)
message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

message_button1 = Button(text="Инструкция", command=instruction)
message_button1.grid(row=3, column=0, padx=5, pady=5, sticky='w')

root.minsize(width=300, height=100)
root.resizable(width=False, height=False)

root.eval('tk::PlaceWindow . center')

root.mainloop()
