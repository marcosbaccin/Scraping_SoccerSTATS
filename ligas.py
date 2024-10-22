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

try:
    driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
except:
    #print("")
    pass

tabela = driver.find_element(By.XPATH, '//*[@id="btable"]/tbody')

ligas = tabela.find_elements(By.TAG_NAME, 'tr')
print(len(ligas))
links = pd.DataFrame(columns=['League', '+1.5', '+2.5', '+3.5', 'BTS'])
qtd_ligas = 0
media_mtog = 0
media_mttg = 0
media_three = 0
media_bts = 0

i = 1
for l in ligas:
    try:
        mtog = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[11]').get_attribute('innerHTML').replace('%', '')
        
        if mtog != '&nbsp;-&nbsp;':
            media_mtog = media_mtog + int(mtog)
            qtd_ligas = qtd_ligas + 1

    except:
        #print("")
        pass
    
    try:
        mttg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[12]/b').get_attribute('innerHTML').replace('%', '')
        
        if mttg != '&nbsp;-&nbsp;':
            media_mttg = media_mttg + int(mttg)
    except:
        try:
            mttg = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[12]').get_attribute('innerHTML').replace('%', '')
        
            if mttg != '&nbsp;-&nbsp;':
                media_mttg = media_mttg + int(mttg)
        except:
            #print("")
            pass
    
    try:
        three = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[13]').get_attribute('innerHTML').replace('%', '')

        if three != '&nbsp;-&nbsp;':
            media_three = media_three + int(three)
    except:
        #print("")
        pass

    try:
        bts = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[14]/font').get_attribute('innerHTML').replace('%', '')

        if bts != '&nbsp;-&nbsp;':
            media_bts = media_bts + int(bts)
    except:
        #print("")
        pass

    try:
        link = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[2]/a').get_attribute('href').replace('https://www.soccerstats.com/latest.asp?league=', '')
        #link_pt1 = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[1]').get_attribute('textContent').replace('&nbsp; ', '')
        #link_pt2 = driver.find_element(By.XPATH, f'//*[@id="btable"]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML')
        #link_final = link_pt1 + link_pt2
        #link_final = link_pt1
        
        links.loc[len(links)] = [f"'{link}',", int(mtog), int(mttg), int(three), int(bts)]
    except:
        #print("")
        pass

    i = i + 1

media_mtog = media_mtog / qtd_ligas
media_mttg = media_mttg / qtd_ligas
media_three = media_three / qtd_ligas
media_bts = media_bts / qtd_ligas

print(f'Frequencia de +1.5 gols: {media_mtog:.2f}%')
print(f'Frequencia de +2.5 gols: {media_mttg:.2f}%')
print(f'Frequencia de +3.5 gols: {media_three:.2f}%')
print(f'Frequencia de Ambas Marcam: {media_bts:.2f}%')

links_mtog = links[links['+1.5'] > media_mtog][['League']]
links_mttg = links[links['+2.5'] > media_mttg][['League']]
links_three = links[links['+3.5'] > media_three][['League']]
links_bts = links[links['BTS'] > media_bts][['League']]

links_mtog.sort_values(['League'], ascending=[True], inplace=True)
links_mtog.to_csv("C:/VScode_projects/soccerstats/links_MTOG.csv", index=False)

links_mttg.sort_values(['League'], ascending=[True], inplace=True)
links_mttg.to_csv("C:/VScode_projects/soccerstats/links_MTTG.csv", index=False)

links_three.sort_values(['League'], ascending=[True], inplace=True)
links_three.to_csv("C:/VScode_projects/soccerstats/links_THREE.csv", index=False)

links_bts.sort_values(['League'], ascending=[True], inplace=True)
links_bts.to_csv("C:/VScode_projects/soccerstats/links_BTS.csv", index=False)

links.drop(columns=['+1.5', '+2.5', '+3.5', 'BTS'], inplace=True)
links.to_csv("C:/VScode_projects/soccerstats/links.csv", index=False)
