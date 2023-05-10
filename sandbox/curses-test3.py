import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    RED_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLUE = curses.color_pair(2)

    pad = curses.newpad(100,100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLUE)
    pad.refresh(0,0,5,5,25,75)
    stdscr.getch()


wrapper(main)
