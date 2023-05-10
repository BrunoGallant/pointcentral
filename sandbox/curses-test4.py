import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    # stdscr.nodelay(True)

    x, y = 0, 0
    a =0
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -=1
        elif key == "KEY_DOWN":
            y +=1
    
        stdscr.clear()
        a += 1
        stdscr.addstr(0, a//1000, "tabarnak")
        stdscr.addstr(curses.LINES -1, 0, f"x: {x}, y: {y}")
        stdscr.addstr(y, x, "0")
        stdscr.refresh()





wrapper(main)
