import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    BOTTOM = curses.LINES -2
    RIGHT = curses.COLS -1
    win = curses.newwin(2,17,3,3)
    box = Textbox(win)

    rectangle(stdscr,2,2,5,20)
    stdscr.refresh()

    box.edit()

    text1 = box.gather().strip().replace("\n", "")

    stdscr.addstr(BOTTOM, 0, f"Illumination: {text1}")


    stdscr.getch()




wrapper(main)

