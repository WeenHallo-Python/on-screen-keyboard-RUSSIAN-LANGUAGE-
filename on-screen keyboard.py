from tkinter import *

window = Tk()
window.title("Экранная клавиатура")

# Глобальная переменная для хранения ввода
entry_text = StringVar()

# Функция для добавления символа в поле ввода
def add_to_entry(symbol):
    current_text = entry_text.get()
    entry_text.set(current_text + symbol)

# Функция для очистки поля ввода
def clear_entry():
    entry_text.set("")

# Функция для удаления последнего символа
def backspace():
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

# Создаем поле ввода
entry = Entry(window, width=40, textvariable=entry_text, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=12, pady=10)

# Строка 1 (Ё-Backspace)
Button(window, text='Ё', height=2, width=5, command=lambda: add_to_entry('ё')).grid(row=1, column=0)
for i in range(10):
    Button(window, text=str(i), height=2, width=5, command=lambda num=i: add_to_entry(str(num))).grid(row=1, column=i+1)
Button(window, text='Backspace', height=2, width=5, command=backspace).grid(row=1, column=11)

# Строка 2 (Tab-Ъ)
Button(window, text='Tab', height=2, width=5, command=lambda: add_to_entry('\t')).grid(row=2, column=0)
letters_row_2 = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ']
for i, letter in enumerate(letters_row_2):
    Button(window, text=letter, height=2, width=5, command=lambda l=letter: add_to_entry(l)).grid(row=2, column=i+1)

# Строка 3 (Caps Lock-Enter)
Button(window, text='Caps Lock', height=2, width=5, command=lambda: add_to_entry('')).grid(row=3, column=0)
letters_row_3 = ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э']
for i, letter in enumerate(letters_row_3):
    Button(window, text=letter, height=2, width=5, command=lambda l=letter: add_to_entry(l)).grid(row=3, column=i+1)
Button(window, text='Enter', height=2, width=5, command=lambda: add_to_entry('\n')).grid(row=3, column=11)

# Строка 4 (Shift-Shift)
Button(window, text='Shift', height=2, width=5, command=lambda: add_to_entry('')).grid(row=4, column=0)
letters_row_4 = ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', '/,.?']
for i, letter in enumerate(letters_row_4):
    Button(window, text=letter, height=2, width=5, command=lambda l=letter: add_to_entry(l)).grid(row=4, column=i+1)
Button(window, text='Shift', height=2, width=5, command=lambda: add_to_entry('')).grid(row=4, column=11)

# Строка 5 (Ctrl-Ctrl)
Button(window, text='Ctrl', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=0)
Button(window, text='Win', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=1)
Button(window, text='Alt', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=2)
Button(window, text='Space', height=2, width=15, command=lambda: add_to_entry(' '), padx=5).grid(row=5, column=3, columnspan=3)
Button(window, text='Alt', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=6)
Button(window, text='FN', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=7)
Button(window, text='Empty', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=8)
Button(window, text='Ctrl', height=2, width=5, command=lambda: add_to_entry('')).grid(row=5, column=11)

# Запускаем главный цикл
window.mainloop()
