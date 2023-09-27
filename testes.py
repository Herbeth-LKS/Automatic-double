from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://blaze.com/pt/games/double')

lista = navegador.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

list = lista.split()

sequencia = list[0:10]

print(sequencia)
