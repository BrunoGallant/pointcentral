import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    RED_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLUE = curses.color_pair(2)

    for i in range(100):
        stdscr.clear()
        color = RED_AND_YELLOW

        if i % 2 == 0:
            color = GREEN_AND_BLUE
        
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)



    stdscr.addstr(10, 10, "tabarnak", curses.A_BOLD)
    stdscr.addstr(11, 10, "tabarnak", RED_AND_YELLOW | curses.A_BOLD)
    stdscr.addstr(12, 10, "tabarnak", GREEN_AND_BLUE | curses.A_BOLD)


    stdscr.getch()


wrapper(main)
