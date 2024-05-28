# Importação das bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests

# Importando e inicializando o driver do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-animations")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

link = 'https://www.soccerstats.com/leagues.asp'

driver.get(link)
time.sleep(2)

try:
    # Clicar em aceitar os cookies da página
    driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
except:
    #print("")
    pass

tabela = driver.find_element(By.XPATH, '//*[@id="btable"]/tbody')

ligas = tabela.find_elements(By.TAG_NAME, 'tr')
print(len(ligas))
qtd_ligas = 0
media_gpg = 0
media_mtog = 0
media_mttg = 0
media_totg = 0

i = 1
for l in ligas:
    try:
        mtog = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[10]').get_attribute('innerHTML').replace('%', '')
        
        if mtog != '&nbsp;-&nbsp;':
            media_mtog = media_mtog + int(mtog)
            qtd_ligas = qtd_ligas + 1

    except Exception as e:
        print(e.message)
    
    try:
        mttg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[11]/b').get_attribute('innerHTML').replace('%', '')
        
        if mttg != '&nbsp;-&nbsp;':
            media_mttg = media_mttg + int(mttg)
    except Exception as e:
        try:
            mttg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[11]').get_attribute('innerHTML').replace('%', '')
        
            if mttg != '&nbsp;-&nbsp;':
                media_mttg = media_mttg + int(mttg)
        except Exception as e:
            print(e.message)

    try:
        totg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[12]').get_attribute('innerHTML').replace('%', '')
        
        if totg != '&nbsp;-&nbsp;':
            media_totg = media_totg + int(totg)

    except Exception as e:
        print(e.message)

    try:
        gpg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[7]/font').get_attribute('innerHTML').replace('%', '')
        
        if gpg != '&nbsp;-&nbsp;':
            media_gpg = media_gpg + float(gpg)

    except Exception as e:
        print(e.message)

    i = i + 1

media_mtog = media_mtog / qtd_ligas
media_mttg = media_mttg / qtd_ligas
media_totg = media_totg / qtd_ligas
media_gpg = media_gpg / qtd_ligas

print(f'Media +1.5 gols: {media_mtog}')
print(f'Media +2.5 gols: {media_mttg}')
print(f'Media +3.5 gols: {media_totg}')
print(f'Media geral de gols por jogo: {media_gpg}')
