import pyautogui as pa
import time
import pyperclip

num_repetitions = int(input("Enter the number of lines: "))

#When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
pa.FAILSAFE = True

for i in range(num_repetitions):  # Replace with the number of repetitions you want
    time.sleep(5)
    pa.keyDown('command')
    pa.press('c')
    pa.keyUp('command')
    pa.click(x=1240, y=55)

    # Paste by typing instead of Cmd+V
    text = pyperclip.paste()
    pa.write(text)

    time.sleep(2)
    pa.hotkey('alt', 'pagedown')
    time.sleep(2)
    pa.hotkey('f6')
    time.sleep(2)
    pa.click(x=570, y=58)
    pa.press('right')

    # Once in account and f6
    pa.keyDown('command')
    pa.press('c')
    pa.keyUp('command')
    pa.click(x=1240, y=55)

    # Paste by typing instead of Cmd+V
    text = pyperclip.paste()
    pa.write(text)

    pa.hotkey('tab')
    time.sleep(3)
    pa.hotkey('tab')
    pa.click(x=570, y=58)
    pa.press('right')

    pa.keyDown('command')
    pa.press('c')
    pa.keyUp('command')
    pa.click(x=1240, y=55)

    # Paste by typing instead of Cmd+V
    text = pyperclip.paste()
    pa.write(text)

    pa.hotkey('tab')
    time.sleep(2)
    pa.click(x=570, y=58)
    pa.press('right')

    pa.keyDown('command')
    pa.press('c')
    pa.keyUp('command')
    pa.click(x=1240, y=55)

    # Paste by typing instead of Cmd+V
    text = pyperclip.paste()
    pa.write(text)

    pa.hotkey('tab')
    time.sleep(2)
    pa.click(x=570, y=58)
    pa.press('right')

    pa.keyDown('command')
    pa.press('c')
    pa.keyUp('command')
    pa.click(x=1240, y=55)

    # Paste by typing instead of Cmd+V
    text = pyperclip.paste()
    pa.write(text)

    pa.hotkey('f10')
    time.sleep(3)
    pa.hotkey('f5')
    pa.click(x=570, y=58)
    pa.press('down')

    pa.keyDown('command')
    pa.press('left')
    pa.keyUp('command')
