parser.add_argument("--cursor", help = "Cursor type (default: 1)(0 - none, 1 - thin, 2 - wide)", type=int, default = 1)
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
    screen = curses.initscr() 
    #Changing cursor appearance
    curses.curs_set(cursor)

    #Outputting text noise
    #"try" - to prevent an error from appearing after stopping the program
    try :
        while True :
            #Creating a word with length in the range from "min_len" to "max_len"
            for i in range(random.randint(min_len,max_len)) :
                print(colors[text_color] + random.choice(alphabet), end="", flush=True)
                #Delay
                time.sleep(sleep_time)
            #Selecting a random punctuation mark
            #Chance depends on the number of characters added in lines 56 - 70
            if marks_table != [] :
                print(colors[text_color] + random.choice(marks_table), end="", flush=True)
                #Delay
                time.sleep(sleep_time)
    #Closing "try"
    except :
        pass

#Closing TUI
curses.wrapper(main)
