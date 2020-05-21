import pyautogui as pag
import time
from tkinter import Tk
from tkinter import Button
from tkinter import Entry





# ПОИСК СТАТЕЙ
def get_search_query():
    search_query = search_box.get()
    search_query_format = search_query.replace('.', '/')
    article_search(search_query_format)


def article_search(article_number):
    """
    :param article_number: Принимает на вход номер статьи и выполняет поиск.
    :return: None

    Данная функция, выполняет поиск статьи, переданной а параметрах.
    Идет во вкладку с БД, открывает поиск по страние, вводит переданную статью,
    прожимает Enter для выполнения поиска, а затем, ctrl+enter для открытия найденой статьи.
    """
    pag.PAUSE = 0.5  # Здесь указываем задержку каждого вызова действия
    std = 0.1  # Стандартная продолжительность действия
    pag.FAILSAFE = True  # Если True, то перемещение в левый верхний угол, убивает скрипт

    # ВКЛАДКА
    # Идем к первой вкладке в браузере, клик.
    pag.moveTo(x=1397, y=26, duration=std)
    pag.click()
    pag.hotkey('ctrl', 'f')
    time.sleep(0.1)
    pag.typewrite(article_number)
    pag.press('enter')
    pag.hotkey('ctrl', 'enter')


root = Tk()
root.geometry('1950x62')
root.title('Auto FOS')

start_button = Button(text="Выполнить обращение", width=25, height=1, command=None)
start_zdi_button = Button(text="ЗДИ", width=25, height=1, command=None)

start_button.grid(row=0, column=1)
start_zdi_button.grid(row=1, column=1)

search_box = Entry(width=25)
search_button = Button(text='Найти статью', width=25, height=1, command=get_search_query)
search_button.grid(row=1, column=0)
search_box.grid(row=0, column=0)


root.mainloop()