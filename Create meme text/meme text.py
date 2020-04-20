import pyautogui
import pyperclip
import keyboard

def meme_str():
    switch = False
    pyautogui.hotkey('ctrl', 'c')
    fill = ""
    for x in pyperclip.paste():
        if not switch:
            fill += x.upper()
            switch = True
        else:
            fill += x.lower()
            switch = False
    pyperclip.copy(fill)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')

keyboard.add_hotkey('ctrl+shift+p', meme_str)
print('Running...')

keyboard.wait('esc')
