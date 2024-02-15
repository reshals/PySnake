import curses
import time

def main(screen):
	curses.curs_set(0)
	time.sleep(1)
	snake = [(0, i) for i in reversed(range(20))]
	screen.addstr(*snake[0], '@')
	for segment in snake[1:]:
   		screen.addstr(*segment, '*')
	#print(snake)

if __name__ == '__main__':
	curses.wrapper(main)
