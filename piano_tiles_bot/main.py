import pyautogui
import time
import keyboard
import PIL.ImageGrab
import win32api
import win32con

tiles_x_pos = [(723, 'a'), (885, 's'), (1028, 'd'), (1194, 'f')]
pyautogui.PAUSE = 0


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def run():
    time.sleep(2)
    global tiles_x_pos
    x = 0
    height = 600
    print('Ready')
    while not keyboard.is_pressed('q'):
        for i in tiles_x_pos:
            if PIL.ImageGrab.grab().load()[i[0], height][0] >= 220 and i[0] != x:
                print(f'Pressing {i[1]}, height = {height}')
                pyautogui.press(i[1])
                x = i[0]
                if height > 40:
                    height -= 10
                # break


if __name__ == '__main__':
    run()
