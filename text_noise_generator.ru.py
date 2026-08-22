#!/usr/bin/env python

#Имторты
import random
import time
import argparse
import curses

#Обьявление переменных/неизменяемые переменные
marks_table = []
colors = {"black": "\u001b[30m", "red": "\u001b[31m", "green": "\u001b[32m", "yellow": "\u001b[33m", "blue": "\u001b[34m", "magenta": "\u001b[35m", "cyan": "\u001b[36m", "white": "\u001b[37m", "light_black": "\u001b[90m", "light_red": "\u001b[91m", "light_green": "\u001b[92m", "light_yellow": "\u001b[93m", "light_blue": "\u001b[94m", "light_magenta": "\u001b[95m", "light_cyan": "\u001b[96m", "light_white": "\u001b[97m"}

#Скрока для сокращения считывания аргументов
parser = argparse.ArgumentParser()
#Считывание аргументов
#(сокращение, полный аргумент ,для help ,тип ,стандартное значение)
parser.add_argument("-t", "--sleep-time", help = "Time between printing characters (default: 0.05)", type = float, default = 0.05)
parser.add_argument("--max-len", help = "Maximum word length (default: 12)", type = int, default = 12)
parser.add_argument("--min-len", help = "Minimum word length (default: 3)", type = int, default = 3)
parser.add_argument("-a", "--alphabet", help = "Alphabet used (en/ru or a string of custom characters) (default: en)", type = str, default = "abcdefghijklmnopqrstuvwxyz")
parser.add_argument("--text-color", help = "Text color (default: white)", type = str, default = "white")
parser.add_argument("-v", "--filling-void", help = "Frequency of spaces (default: 12)", type = int, default = 12)
parser.add_argument("-p", "--filling-points", help = "Frequency of periods (default: 5)", type = int, default = 5)
parser.add_argument("-c", "--filling-commas", help = "Frequency of commas (default: 3)", type = int, default = 3)
parser.add_argument("-q", "--filling-question", help = "Frequency of question marks (default: 1)", type = int, default = 1)
parser.add_argument("-e", "--filling-exclamation-marks", help = "Frequency of exclamation marks (default: 1)", type = int, default = 1)
parser.add_argument("-s", "--spaces-after-punctuation-marks", help = "Spaces after punctuation marks (default: True)(if started with -s or an unabridged argument, then False)", action="store_false", default = True)
parser.add_argument("--cursor", help = "Тип курсора (default: 1)(0 - нет, 1 - тонкий, 2 - широкий)", type=int, default = 1)
#Строка для сокращения привязки аргумента к переменной
args = parser.parse_args()

#Обьявление переменных из аргументов
sleep_time = args.sleep_time
max_len = args.max_len
min_len = args.min_len
alphabet = args.alphabet
text_color = args.text_color
filling_void = args.filling_void
filling_points = args.filling_points
filling_commas = args.filling_commas
filling_question = args.filling_question
filling_exclamation_marks = args.filling_exclamation_marks
spaces_after_punctuation_marks = args.spaces_after_punctuation_marks
cursor = args.cursor

#Для смены языка
if alphabet == "ru" :
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

#Для пробелов после знаков припинания
if spaces_after_punctuation_marks == True :
    spaces_after_punctuation_marks = " "
if spaces_after_punctuation_marks == False :
    spaces_after_punctuation_marks = ""

#Эти 4 "for" для настройки частоты появления знаков припинания
for i in range(filling_void) :
    marks_table.append(" ")

for i in range(filling_points) :
    marks_table.append("." + spaces_after_punctuation_marks)

for i in range(filling_commas) :
    marks_table.append("," + spaces_after_punctuation_marks) 

for i in range(filling_question) :
    marks_table.append("?" + spaces_after_punctuation_marks)

for i in range(filling_exclamation_marks) :
    marks_table.append("!" + spaces_after_punctuation_marks)

#Основная функция
#(stdscr) - передаём окно терминала
def main(stdscr) :
    #Создаём TUI интерфейс
    curses.start_color()
    curses.use_default_colors()
    screen = curses.initscr() 
    #Изсенение вида курсора
    curses.curs_set(cursor)

    #Выводим текстовый шум
    #"try" - для того чтобы после остановки программы не вылезала ошибка
    try :
        while True :
            #Создание слова в длинну в промежутке от "min_len" до "max_len"
            for i in range(random.randint(min_len,max_len)) :
                print(colors[text_color] + random.choice(alphabet), end="", flush=True)
                #Задержка
                time.sleep(sleep_time)
            #Выбор рандомного знака припинания
            #Шанс зависит от колличества символов добавленных в 56 - 70 строке
            if marks_table != [] :
                print(colors[text_color] + random.choice(marks_table), end="", flush=True)
                #Задержка
                time.sleep(sleep_time)
    #Закрытие "try"
    except :
        pass

#Закрытие TUI
curses.wrapper(main)
