import os
import time
import pyautogui
wh = pyautogui.size()
print(wh)

os.chdir('/Users/ilja/Dropbox/atbs')

print("-------------------- MOVE MOUSE --------------------")

# get screen size
# print(pyautogui.size())

# moves clockwise in a square pattern in top LHS!
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# moves from wherever the mouse is right now!
# for i in range(10):
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)

# get mouse position
# p = pyautogui.position()
# print(p)

print("-------------------- CLICK MOUSE --------------------")
# specify the location of the click if you want to. also can specify the button with eg button='right'
# pyautogui.click(700, 700)


print("-------------------- DRAG MOUSE --------------------")
# ie click and drag
# time.sleep(3)
# pyautogui.click()
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag((distance, 0), duration=0.2, button="left")
#     distance = distance - change
#     pyautogui.drag((0, distance), duration=0.2, button="left")
#     distance = distance - change
#     pyautogui.drag((-distance, 0), duration=0.2, button="left")
#     distance = distance - change
#     pyautogui.drag((0, -distance), duration=0.2, button="left")
#     distance = distance - change


print("-------------------- SCROLL MOUSE --------------------")
# pyautogui.scroll(200)


print("-------------------- FIND COORDS --------------------")
# call the below function from interactive shell to get a pop up window that helps you figure out coordinates on the screen
# pyautogui.mouseInfo()


print("-------------------- TAKE A SCREEN --------------------")
# im = pyautogui.screenshot()

# you could take a screenshot and then compare the value of a particulr pixel with your expectation. If it matches - great, click the button. if not - you know something is off.
# get pixel value
# p = pyautogui.pixel(245, 480)
# print(p)
# print(pyautogui.pixelMatchesColor(245, 480, (72, 165, 217)))  # must exactly match
#

print("-------------------- LOCATE --------------------")
# note the image has to match EXACTLY
# box = pyautogui.locateOnScreen('filename.jpg')
print(box)

# you can then click on it by either extracting the coordinates:
# NOTE it will automatically click the middle of the below
# pyautogui.click((910, 50, 158, 24))

# or pasing the file in directly
# pyautogui.click('filename.jpg')

# NOTE if multiple copies are found, a generator object is generated and it needs to be passed to a list

# NOTE this is a real shitty way to control your ui tho as even 1 pixel change will make it fail
# a better way is to use window features - but they're only available on windows


print("-------------------- ALERTS --------------------")
# pyautogui.alert('this is a pop up!')
# pyautogui.prompt('this is a pop up with an input box!')
# pyautogui.password('this is a pop up with a pw input box!')

print("-------------------- KEYBOARD --------------------")
# pyautogui.write('hello world!!!', 0.25) #second argument adds a delay after each letter, in seconds (so 1/4th of a second)
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y']) #here "left" means left arrow key. That's how you pass non-character keys in.
# NOTE in the second case you need to add []

# we can get more granular with our control of keyboard presses - specifying up, down, or a full press
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')  # prints $$$$$

# there is a special function to press keys in order and then release them in reverse-order
# pyautogui.hotkey('command', 'c')  # will copy something

"""
These scripts can be finicky. Some advice to making it work:
1. Use same screen resolution each time
2. Maximize each window
3. Add generaous pauses for content to load
4. Use locateOnScreen() to find buttons rather than xy coords. If your script can't find it - stop it.
5. Window methods (that don't fucking work on mac) - even better!
6. Use logging to know what your script has done
7. Add as many checks as possible. Really like the one with the screenshot / pixel color checking
8. Supervise your script the first time it runs
9. Use sleep and countdown funcs: pyautogui.sleep / pyautogui.countdown

All keys:

moveTo(x, y) Moves the mouse cursor to the given x and y coordinates.

move(xOffset, yOffset) Moves the mouse cursor relative to its current position.

dragTo(x, y) Moves the mouse cursor while the left button is held down.

drag(xOffset, yOffset) Moves the mouse cursor relative to its current position while the left button is held down.

click(x, y, button) Simulates a click (left button by default).

rightClick() Simulates a right-button click.

middleClick() Simulates a middle-button click.

doubleClick() Simulates a double left-button click.

mouseDown(x, y, button) Simulates pressing down the given button at the position x, y.

mouseUp(x, y, button) Simulates releasing the given button at the position x, y.

scroll(units) Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.

write(message) Types the characters in the given message string.

write([key1, key2, key3]) Types the given keyboard key strings.

press(key) Presses the given keyboard key string.

keyDown(key) Simulates pressing down the given keyboard key.

keyUp(key) Simulates releasing the given keyboard key.

hotkey([key1, key2, key3]) Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.

screenshot() Returns a screenshot as an Image object. (See Chapter 19 for information on Image objects.)

getActiveWindow(), getAllWindows(), getWindowsAt(), and getWindowsWithTitle() These functions return Window objects that can resize and reposition application windows on the desktop.

getAllTitles() Returns a list of strings of the title bar text of every window on the desktop.

"""
