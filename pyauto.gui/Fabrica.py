import pyautogui

pyautogui.press('win')
pyautogui.sleep(0.5)
pyautogui.write('Google Chrome',interval=0.1)
pyautogui.press('enter')
pyautogui.sleep(2)

pyautogui.click(1054,594)
pyautogui.write('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval=0.1)
pyautogui.press('enter')


pyautogui.hotkey('win','shift','s')
pyautogui.mouseDown(0,0)
pyautogui.moveTo(1910,1070)
pyautogui.mouseUp()