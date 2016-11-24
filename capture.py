import curses
import os
import cv2
os.environ.setdefault('ESCDELAY', '0')

cap = cv2.VideoCapture(0)

def capture_sign(sign, i):
  r, frame = cap.read()
  if not r:
    raise IOError('Failed to capture image')
  r = cv2.imwrite(sign+'_{:02d}.jpg'.format(i), frame)
  if not r:
    raise IOError('Failed to capture image')

def main(stdscr):
  while True:
    stdscr.addstr("Enter next sign, or emtpy string to quit\n")
    c = stdscr.getch()
    if c==10:
      break

    sign = ""
    while True:
      sign += chr(c)
      stdscr.addstr(chr(c))
      if c==10:
        break
      c = stdscr.getch()
    sign = sign.rstrip()
    stdscr.addstr("Press ESC to capture next image, or ENTER to finish\n")
    i = 1
    while True:
      c = stdscr.getch()
      if c==10:
        break
      if c==27:
        capture_sign(sign, i)
        stdscr.addstr("Wrote {:}_{:02d}.jpg\n".format(sign, i))
        i+=1


curses.wrapper(main)
