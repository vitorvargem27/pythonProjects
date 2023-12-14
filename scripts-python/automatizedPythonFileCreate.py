import pyautogui as mouse
import pyautogui as timeLoad
import pyautogui as keyboard
import pyautogui as action

#pedindo o nome do projeto
projectName = str(input('Write a name of your new python project :\n')).strip().title()

timeLoad.sleep(2)

#clicando para criar novo projeto
mouse.moveTo(3132, 140)
mouse.click(button='right')
keyboard.press("down")
timeLoad.sleep(1)
keyboard.press('enter')

#clicando para criar um novo arquivo python
keyboard.press("down")
timeLoad.sleep(0.1)
keyboard.press("down")
timeLoad.sleep(0.1)
keyboard.press("down")
timeLoad.sleep(0.1)
keyboard.press("down")
keyboard.press("enter")

#aplicando o nome ao arquivo python
timeLoad.sleep(1)
action.typewrite(projectName, interval = 0)
keyboard.press("enter")

#criando código automaticamente
timeLoad.sleep(2)
action.typewrite("import pyautogui as action\n"
                 "import pyautogui as timeLoad\n"
                 "\n"
                 "timeLoad.sleep(2)\n"
                 "action.press('win')\n"
                 "\n"
                 "timeLoad.sleep(1)\n"
                 "action.typewrite('google')\n"
                 "timeLoad.sleep(1)\n"
                 "action.press('enter')\n"
                 "\n"
                 "timeLoad.sleep(3)\n"
                 "action.keyDown('ctrl')\n"
                 "action.press('t')\n"
                 "action.keyUp('ctrl')\n"
                 )