import os
from sty import fg, bg, ef, rs
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from telethon import TelegramClient, events

time = int(input("quanto tempo o browser deve esperar?(em segundos)"))
valoraposta = int(input("qual valor vc deseja apostar?"))
valorbranco = float(input("valor do branco"))


dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))
options.add_argument("--maximize_window()")
#options.add_argument("--handlles")
driver = webdriver.Chrome(options=options)

driver.get("https://blaze.com/pt/games/double")




sleep(time)

#valor da aposta
aposta = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
#botao metade
metade = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]')
#botao de jogar
jogar = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button')
#botao do preto

preto = driver.find_element(By.CLASS_NAME, "black")

#botao do vermelho

vermelho = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]')

branco = driver.find_element(By.CLASS_NAME, "white")

branco.click()


api_id = 'your api id'
api_hash = 'your hash'


client = TelegramClient('anon', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id

    if chat_id == -1001634471545:

        msg = event.raw_text
        if "entrar preto e branco" in msg:
            aposta.click()
            sleep(0.3)
            aposta.clear()
            sleep(0.3)
            aposta.send_keys(valoraposta)
            sleep(0.3)
            preto.click()
            sleep(0.3)
            jogar.click()
            sleep(0.2)
            aposta.click()
            sleep(0.2)
            aposta.clear()
            sleep(0.2)
            aposta.send_keys(valorbranco)
            sleep(0.2)
            branco.click()
            sleep(0.3)
            jogar.click()
            print(fg.li_yellow + 'APOSTA FEITA!' + fg.rs)

        if "entrar vermelho e branco" in msg:
            aposta.click()
            sleep(0.3)
            aposta.clear()
            sleep(0.3)
            aposta.send_keys(valoraposta)
            sleep(0.3)
            vermelho.click()
            sleep(0.3)
            jogar.click()
            sleep(0.2)
            aposta.click()
            sleep(0.2)
            aposta.clear()
            sleep(0.2)
            aposta.send_keys(valorbranco)
            sleep(0.2)
            branco.click()
            sleep(0.3)
            jogar.click()
            print(fg.li_yellow + 'APOSTA FEITA!' + fg.rs)

        if "Vamos para a primeira gale P." in msg:
            valorgale = valoraposta*2
            aposta.click()
            sleep(0.3)
            aposta.clear()
            sleep(0.3)
            aposta.send_keys(valorgale)
            sleep(0.3)
            preto.click()
            sleep(0.3)
            jogar.click()
            sleep(0.3)
            metade.click()
            sleep(0.3)
            branco.click()
            sleep(0.3)
            jogar.click()
            print(fg.li_yellow + 'APOSTA FEITA!' + fg.rs)

        if "Vamos para a primeira gale V." in msg:
            valorgale = valoraposta*2
            aposta.click()
            sleep(0.3)
            aposta.clear()
            sleep(0.3)
            aposta.send_keys(valorgale)
            sleep(0.3)
            vermelho.click()
            sleep(0.3)
            jogar.click()
            sleep(0.3)
            metade.click()
            sleep(0.3)
            branco.click()
            sleep(0.3)
            jogar.click()
            print(fg.li_yellow + 'APOSTA FEITA!' + fg.rs)


        if "WINN" in msg:
            print(fg.green + 'GREEN' + fg.rs)

        if "LOSS" in msg:
            print(fg.red + 'RED' + fg.rs)

client.start()
client.run_until_disconnected()
