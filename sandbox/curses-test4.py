import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)



    key = stdscr.getkey()

    stdscr.addstr(5, 5, f"Key: {key}")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
