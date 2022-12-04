import pyautogui
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

pyautogui.PAUSE = 2

contador = 0

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
driver.maximize_window()

while contador < 5:
    # Clicar no email na posição
    pyautogui.click(x=375, y=269)
    # Clicar para baixar o arquivo
    pyautogui.click(x=935, y=346)
    # Clicar em "baixar"
    pyautogui.click(x=741, y=462)
    # Clicar no local com o nome do email
    pyautogui.click(x=769, y=300)
    # Clicar para copiar o email
    pyautogui.click(x=1114, y=457)
    # Clicar fora do card
    pyautogui.click(x=778, y=638)
    # Abrir novo e-mail
    pyautogui.press('n')
    # Keys -> ctrl + V
    pyautogui.hotkey("ctrl","v")
    # Keys -> Tab  (2x)
    pyautogui.press('tab')
    pyautogui.press('tab')
    # Digitar o título
    pyperclip.copy("RECEBIMENTO DE NOTA FISCAL")
    pyautogui.hotkey('ctrl','v')
    # Keys -> Enter ou Tab
    pyautogui.press('tab')
    # Digitar o "texto"
    pyperclip.copy("Olá")
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyperclip.copy('Aqui é da Rádio e vim confirmar o recebimento da nota fiscal referente ao último mês.')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyperclip.copy('Atenciosamente!')
    pyautogui.hotkey('ctrl','v')
    # Clicar no anexar
    pyautogui.click(x=1196, y=177)
    # Clicar navegar neste computador
    pyautogui.click(x=1213, y=218)
    # Clicar no ultimo arquivo baixado
    pyautogui.click(x=350, y=186)
    # Anexar
    pyautogui.press('enter')
    # Clicar em enviar
    pyautogui.click(x=671, y=230)
    # Posicionar o mouse no email que está
    pyautogui.moveTo(x=375, y=269)
    # Scroll pra cima
    pyautogui.scroll(140)
    # REPETE O PROCESSO 
    contador = contador + 1
