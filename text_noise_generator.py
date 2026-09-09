#!/usr/bin/env python

#Imports
import random
import time
import argparse
import curses

#Declaration of variables/immutable variables
marks_table = []

#Line to shorten argument parsing
parser = argparse.ArgumentParser()
#Parsing arguments
#(shortcut, full argument, for help, type, default value)
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
parser.add_argument("-s", "--spaces-after-punctuation-marks", help = "Spaces after punctuation marks (default: True)", action="store_false", default = True)
parser.add_argument("--cursor", help = "Cursor type (default: 1)(0 - none, 1 - thin, 2 - wide)", type = int, default = 1)
parser.add_argument("-f","--save-into-file",help = "Allows to generate text immediately in a txt file", type = str, default = "")
parser.add_argument("-l","--write-capital-letters",help="Сapitalize letters after dots, questions, and exclamation marks (default: True)", action="store_false", default = True)
#Line to shorten binding of argument to variable
args = parser.parse_args()

#Declaration of variables from arguments
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
save_into_file = args.save_into_file
write_capital_letters = args.write_capital_letters

#For switching language
if alphabet == "ru" :
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

#For spaces after punctuation marks
if spaces_after_punctuation_marks == True :
    spaces_after_punctuation_marks = " "
if spaces_after_punctuation_marks == False :
    spaces_after_punctuation_marks = ""

#These 4 "for" loops are for configuring the frequency of punctuation marks
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

#Main function
#(stdscr) - pass the terminal window
def main(stdscr) :
    #Creating TUI interface
    curses.start_color()
    curses.use_default_colors()
    #Changing cursor appearance
    curses.curs_set(cursor)

    #Local variables
    random_text = ""
    colors = {"black": "\u001b[30m", "red": "\u001b[31m", "green": "\u001b[32m", "yellow": "\u001b[33m", "blue": "\u001b[34m", "magenta": "\u001b[35m", "cyan": "\u001b[36m", "white": "\u001b[37m", "light_black": "\u001b[90m", "light_red": "\u001b[91m", "light_green": "\u001b[92m", "light_yellow": "\u001b[93m", "light_blue": "\u001b[94m", "light_magenta": "\u001b[95m", "light_cyan": "\u001b[96m", "light_white": "\u001b[97m"}

    #Checking the path for writing text to a file
    if save_into_file != "" :
        with open(save_into_file, "a", encoding="utf-8") as file :
            #"try" - to prevent an error from appearing after stopping the program
            try :
                while True :
                    #Creating a word with length in the range from "min_len" to "max_len"
                    for i in range(random.randint(min_len,max_len)) :
                        #Checking the argument and punctuation mark for changing case
                        if write_capital_letters == True and ("." in random_text or "?" in random_text or "!" in random_text) :
                            random_text = colors[text_color] + random.choice(alphabet).upper()
                        else :
                            random_text = colors[text_color] + random.choice(alphabet)
                        #Output and writing of text
                        print(random_text, end="", flush=True)
                        file.write(random_text)
                        time.sleep(sleep_time)

                    #Selecting a random punctuation mark
                    #Chance depends on the number of characters added in lines 56 - 70
                    if marks_table != [] :
                        random_text = colors[text_color] + random.choice(marks_table)
                        print(random_text, end="", flush=True)
                        file.write(random_text)
                        time.sleep(sleep_time)

            #Closing "try"
            except :
                KeyboardInterrupt
    else :
        #Outputting text noise
        #"try" - to prevent an error from appearing after stopping the program
        try :
            while True :
               #Creating a word with length in the range from "min_len" to "max_len"
                for i in range(random.randint(min_len,max_len)) :
                    #Checking the argument and punctuation mark for changing case
                    if write_capital_letters == True and ("." in random_text or "?" in random_text or "!" in random_text) :
                        random_text = colors[text_color] + random.choice(alphabet).upper()
                    else :
                        random_text = colors[text_color] + random.choice(alphabet)
                    #Outputting text
                    print(random_text, end="", flush=True)
                    time.sleep(sleep_time)

                #Selecting a random punctuation mark
                #Chance depends on the number of characters added in lines 56 - 70
                if marks_table != [] :
                    random_text = colors[text_color] + random.choice(marks_table)
                    print(random_text, end="", flush=True)
                    time.sleep(sleep_time)

        #Closing "try" 
        except :
            KeyboardInterrupt

curses.wrapper(main)
