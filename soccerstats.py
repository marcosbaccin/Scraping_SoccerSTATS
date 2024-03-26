# Importação das bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import requests

# Importando e inicializando o driver do Chrome
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Estrutura padrão de link para acessar as estatísticas de gols das ligas no Soccerstats
goals_link = "https://www.soccerstats.com/trends.asp?league="
latest_link = 'https://www.soccerstats.com/latest.asp?league='

# Ligas disponíveis no Soccerstats
leagues = ['albania', 'algeria', 'algeria3', 'andorra', 'argentina', 'argentina2', 'argentina3', 'argentina4', 'argentina5', 'argentina10', 
           'armenia', 'australia', 'australia2', 'australia3', 'australia4', 'australia5', 'australia6', 'australia7', 'australia8', 'australia10', 
           'australia11', 'austria', 'austria2', 'austria6', 'austria7', 'austria8', 'azerbaijan', 'bahrain', 'bangladesh', 'belarus', 
           'belarus2', 'belarus4', 'belgium', 'belgium2', 'belgium3', 'belgium4', 'belgium6', 'bolivia', 'bolivia2', 'bosnia', 
           'bosnia2', 'brazil', 'brazil2', 'brazil3', 'brazil4', 'brazil5', 'brazil6', 'brazil7', 'brazil8', 'brazil9', 
           'brazil10', 'brazil11', 'brazil12', 'brazil14', 'brazil15', 'brazil16', 'brazil17', 'brazil18', 'brazil19', 'brazil20', 
           'brazil21', 'bulgaria', 'bulgaria2', 'canada', 'chile', 'chile2', 'chile3', 'china', 'china2', 'colombia', 
           'colombia2', 'costarica', 'costarica2', 'croatia', 'croatia2', 'cyprus', 'cyprus2', 'czechrepublic', 'czechrepublic2', 'czechrepublic3', 
           'czechrepublic4', 'denmark', 'denmark2', 'denmark3', 'ecuador', 'ecuador2', 'ecuador3', 'egypt', 'england', 'england2', 
           'england3', 'england4', 'england5', 'england6', 'england7', 'england8', 'england9', 'england10', 'england11', 'england15', 
           'england17', 'england18', 'england19', 'estonia', 'estonia2', 'ethiopia', 'faroeislands', 'faroeislands2', 'finland', 'finland2',
           'finland3', 'finland4', 'finland5', 'finland6', 'france', 'france2', 'france3', 'france4', 'france5', 'france6',
           'france7', 'france14', 'georgia', 'georgia2', 'germany', 'germany2', 'germany3', 'germany4', 'germany5', 'germany6',
           'germany7', 'germany8', 'germany9', 'germany10', 'germany11', 'germany12', 'germany15', 'germany16', 'germany17', 'germany18', 
           'germany19', 'germany20', 'germany21', 'germany22', 'germany23', 'germany24', 'ghana', 'gibraltar', 'greece', 'greece2',
           'greece3', 'guatemala', 'guatemala2', 'honduras', 'honduras2', 'hongkong', 'hungary', 'hungary2', 'iceland', 'iceland2', 
           'iceland3', 'iceland4', 'iceland5', 'iceland6', 'india', 'india2', 'indonesia', 'iran', 'iraq', 'ireland',
           'ireland2', 'ireland3', 'israel', 'israel2', 'israel3', 'israel4', 'italy', 'italy2', 'italy3', 'italy4',
           'italy5', 'italy6', 'italy7', 'italy8', 'italy9', 'italy10', 'italy11', 'italy12', 'italy13', 'italy14',
           'italy15', 'italy16', 'italy17', 'ivorycoast', 'jamaica', 'japan', 'japan2', 'japan3', 'japan4', 'japan5',
           'jordan', 'kazakhstan', 'kenya', 'kosovo', 'kuwait', 'latvia', 'latvia2', 'lithuania', 'lithuania2', 'luxembourg',
           'malaysia', 'malaysia2', 'malta', 'malta2', 'mauritius', 'mexico', 'mexico2', 'mexico5', 'mexico6', 'moldova',
           'mongolia', 'montenegro', 'morocco', 'morocco2', 'myanmar', 'netherlands', 'netherlands2', 'netherlands3', 'netherlands4', 'netherlands6', 
           'newzealand', 'nicaragua', 'nicaragua2', 'nigeria', 'northernireland', 'northernireland2', 'northernireland3', 'northmacedonia', 'norway', 'norway2', 
           'norway3', 'norway4', 'norway5', 'norway6', 'norway7', 'norway8', 'norway9', 'norway10', 'norway11', 'norway12',
           'oman', 'panama', 'panama2', 'paraguay', 'paraguay2', 'paraguay3', 'peru', 'peru2', 'peru3', 'poland',
           'poland2', 'poland3', 'poland4', 'portugal', 'portugal2', 'portugal4', 'portugal5', 'portugal6', 'portugal7', 'portugal8', 
           'qatar', 'qatar2', 'romania', 'russia', 'russia2', 'rwanda', 'sanmarino', 'saudiarabia', 'saudiarabia2', 'scotland', 
           'scotland2', 'scotland3', 'scotland4', 'scotland7', 'serbia', 'serbia2', 'singapore', 'slovakia', 'slovakia2', 'slovenia', 
           'southafrica', 'southafrica2', 'southkorea', 'southkorea2', 'southkorea3', 'southkorea4', 'spain', 'spain2', 'spain3', 'spain4', 
           'spain5', 'spain6', 'spain7', 'spain8', 'spain9', 'spain10', 'spain11', 'sweden', 'sweden2', 'sweden3', 
           'sweden4', 'sweden5', 'sweden6', 'sweden7', 'sweden8', 'sweden9', 'sweden10', 'sweden11', 'sweden12', 'switzerland',
           'switzerland2', 'switzerland4', 'syria', 'tajikistan', 'tanzania', 'thailand', 'thailand2', 'turkey', 'turkey2', 'turkey3',
           'turkey4', 'turkey5', 'turkey6', 'turkey7', 'turkey8', 'turkey10', 'uae', 'uae2', 'uganda', 'ukraine', 
           'ukraine2', 'uruguay', 'uruguay2', 'uruguay3', 'usa', 'usa2', 'usa3', 'usa5', 'uzbekistan', 'venezuela',
           'vietnam', 'vietnam2', 'vietnam3', 'wales', 'zambia', 'zimbabwe']

# teste = []

for t in leagues:
    
    #driver = webdriver.Chrome(service=s)
    link = goals_link + t

    mtog_teams_home = [] # mtog (more than one goal)
    mtog_teams_away = []

    mttg_teams_home = [] # mttg (more than two goals)
    mttg_teams_away = []

    bts_teams_home = [] # bts (both teams score)
    bts_teams_away = []

    oght_teams_home = [] # oght (one goal HT(half-time))
    oght_teams_away = []

    if requests.get(link).status_code == 200:

        driver.get(link)
        time.sleep(2)

        try:
            driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
        except:
            #print("")
            pass

        try:
            driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
        except:
            #print("")
            pass
        
        try:
            league_name = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/div[2]/font').get_attribute('innerHTML')
        except NoSuchElementException as e:
            try:
                league_name = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/font').get_attribute('innerHTML')                                            
            except NoSuchElementException as e:
                league_name = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div[2]/font').get_attribute('innerHTML')

        try:
            if int(driver.find_element(By.XPATH, '//*[@id="btable"]/tbody/tr[1]/td[2]/font').get_attribute("innerHTML")) > 5:
                
                # Coletando os dados de +1.5 gols totais

                try:
                    total_goals_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table")
                except NoSuchElementException as e:
                    try:
                        total_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table")
                    except NoSuchElementException as e:
                        total_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table')
                
                teams_total = []
                more_one_goal_total = []
                more_two_goals_total = []
                bts_total = []
                
                try:
                    avg_more_one_goal_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_more_two_goals_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_bts_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_more_one_goal_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_more_one_goal_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tfoot/tr[2]/td[4]/font/span').get_attribute('innerHTML').replace('%', ''))
                        avg_more_two_goals_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tfoot/tr[2]/td[5]/font/span').get_attribute('innerHTML').replace('%', ''))
                        avg_bts_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tfoot/tr[2]/td[9]/font/span').get_attribute('innerHTML').replace('%', ''))

                total_goals_stats_teams = total_goals_stats.find_elements(By.CLASS_NAME, "odd")
                # print(len(total_match_goals_stats_teams))

                i = 1
                for item in total_goals_stats_teams:
                    teams_total.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                    i = i + 1

                #print(teams_total)
                #print(more_one_goal_total)
                #print(avg_more_one_goal_total)

                # Coletando dados de +1.5 gols dos últimos 8 jogos

                try:
                    last8_goals_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table")
                except NoSuchElementException as e:
                    try:
                        last8_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table")
                    except NoSuchElementException as e:
                        last8_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table")

                teams_last8 = []
                more_one_goal_last8 = []
                more_two_goals_last8 = []
                bts_last8 = []
                
                try:
                    avg_more_one_goal_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_more_two_goals_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_bts_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_more_one_goal_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_more_one_goal_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_last8 = float(last8_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))

                last8_goals_stats_teams = last8_goals_stats.find_elements(By.CLASS_NAME, "odd")

                i = 1
                for item in last8_goals_stats_teams:
                    teams_last8.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                    i = i + 1

                #print(teams_last8)
                #print(more_one_goal_last8)
                #print(avg_more_one_goal_last8)

                # Coletando dados de +1.5 gols como mandantes

                try:
                    home_goals_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table")
                except NoSuchElementException as e:
                    try:
                        home_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table")
                    except NoSuchElementException as e:
                        home_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table")

                teams_home = []
                more_one_goal_home = []
                more_two_goals_home = []
                bts_home = []
                
                try:
                    avg_more_one_goal_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_more_two_goals_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_bts_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_more_one_goal_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_more_one_goal_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_home = float(home_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))

                home_goals_stats_teams = home_goals_stats.find_elements(By.CLASS_NAME, "odd")

                i = 1
                for item in home_goals_stats_teams:
                    teams_home.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                    i = i + 1

                #print(teams_home)
                #print(more_one_goal_home)
                #print(avg_more_one_goal_home)

                # Coletando dados de +1.5 gols como visitantes

                try:
                    away_goals_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table")
                except NoSuchElementException as e:
                    try:
                        away_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table")
                    except NoSuchElementException as e:
                        away_goals_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table")

                teams_away = []
                more_one_goal_away = []
                more_two_goals_away = []
                bts_away = []
                
                try:
                    avg_more_one_goal_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_more_two_goals_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                    avg_bts_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_more_one_goal_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_more_one_goal_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tfoot/tr[2]/td[4]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_more_two_goals_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tfoot/tr[2]/td[5]/font/span').get_attribute("innerHTML").replace("%", ""))
                        avg_bts_away = float(away_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tfoot/tr[2]/td[9]/font/span').get_attribute("innerHTML").replace("%", ""))

                away_goals_stats_teams = away_goals_stats.find_elements(By.CLASS_NAME, "odd")

                i = 1
                for item in away_goals_stats_teams:
                    teams_away.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                            more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                            bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                    i = i + 1

                # +0.5 goal in HT
                try:
                    total_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table")
                except NoSuchElementException as e:
                    try:
                        total_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table")
                    except NoSuchElementException as e:
                        try:
                            total_goals_ht_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[1]/table')
                        except NoSuchElementException as e:
                            total_goals_ht_stats = 0

                if total_goals_ht_stats != 0:
                    
                    teams_ht_total = []
                    one_goal_ht_total = []
                    
                    try:
                        avg_one_goal_ht_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        try:
                            avg_one_goal_ht_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                        except NoSuchElementException as e:
                            avg_one_goal_ht_total = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[1]/table/tfoot/tr[2]/td[3]/font/span').get_attribute('innerHTML').replace('%', ''))

                    total_goals_ht_stats_teams = total_goals_ht_stats.find_elements(By.CLASS_NAME, "odd")
                    # print(len(total_match_goals_stats_teams))

                    i = 1
                    for item in total_goals_ht_stats_teams:
                        teams_ht_total.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                        
                        try:
                            one_goal_ht_total.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            try:
                                one_goal_ht_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[1]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                            except NoSuchElementException as e:
                                one_goal_ht_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[1]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))

                        i = i + 1

                # +0.5 goal in HT Home
                try:
                    home_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table")
                except NoSuchElementException as e:
                    try:
                        home_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table")
                    except NoSuchElementException as e:
                        home_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table")
                
                teams_ht_home = []
                one_goal_ht_home = []
                
                try:
                    avg_one_goal_ht_home = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_one_goal_ht_home = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_one_goal_ht_home = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tfoot/tr[2]/td[3]/font/span').get_attribute('innerHTML').replace('%', ''))

                home_goals_ht_stats_teams = home_goals_ht_stats.find_elements(By.CLASS_NAME, "odd")
                # print(len(total_match_goals_stats_teams))

                i = 1
                for item in home_goals_ht_stats_teams:
                    teams_ht_home.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        one_goal_ht_home.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            one_goal_ht_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            one_goal_ht_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))

                    i = i + 1
                
                # +0.5 goal in HT Away
                try:
                    away_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table")
                except NoSuchElementException as e:
                    try:
                        away_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table")
                    except NoSuchElementException as e:
                        away_goals_ht_stats = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table")
                
                teams_ht_away = []
                one_goal_ht_away = []
                
                try:
                    avg_one_goal_ht_away = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                except NoSuchElementException as e:
                    try:
                        avg_one_goal_ht_away = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tfoot/tr[2]/td[3]/font/span').get_attribute("innerHTML").replace("%", ""))
                    except NoSuchElementException as e:
                        avg_one_goal_ht_away = float(total_goals_stats.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tfoot/tr[2]/td[3]/font/span').get_attribute('innerHTML').replace('%', ''))

                away_goals_ht_stats_teams = away_goals_ht_stats.find_elements(By.CLASS_NAME, "odd")
                # print(len(total_match_goals_stats_teams))

                i = 1
                for item in away_goals_ht_stats_teams:
                    teams_ht_away.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                    
                    try:
                        one_goal_ht_away.append(float(item.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        try:
                            one_goal_ht_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))
                        except NoSuchElementException as e:
                            one_goal_ht_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tbody/tr[{i}]/td[4]').get_attribute("sorttable_customkey")))

                    i = i + 1

                # Salvando os dados em dataframes

                df_total = pd.DataFrame({"Teams": teams_total, "+1.5 Total": more_one_goal_total, "+2.5 Total": more_two_goals_total,
                                         "BTS Total": bts_total}, index=None)
                df_total.sort_values(by="Teams", inplace=True, ignore_index=True)

                df_last8 = pd.DataFrame({"Teams Last8": teams_last8, "+1.5 Last8": more_one_goal_last8, "+2.5 Last8": more_two_goals_last8,
                                         "BTS Last8": bts_last8}, index=None)
                df_last8.sort_values(by="Teams Last8", inplace=True, ignore_index=True)

                df_home = pd.DataFrame({"Teams Home": teams_home, "+1.5 Home": more_one_goal_home, "+2.5 Home": more_two_goals_home,
                                        "BTS Home": bts_home}, index=None)
                df_home.sort_values(by="Teams Home", inplace=True, ignore_index=True)

                df_away = pd.DataFrame({"Teams Away": teams_away, "+1.5 Away": more_one_goal_away, "+2.5 Away": more_two_goals_away,
                                        "BTS Away": bts_away}, index=None)
                df_away.sort_values(by="Teams Away", inplace=True, ignore_index=True)

                df_ht_total = pd.DataFrame({"Teams": teams_ht_total, "+0.5 HT Total": one_goal_ht_total}, index=None)
                df_ht_total.sort_values(by="Teams", inplace=True, ignore_index=True)

                df_ht_home = pd.DataFrame({"Teams": teams_ht_home, "+0.5 HT Home": one_goal_ht_home}, index=None)
                df_ht_home.sort_values(by="Teams", inplace=True, ignore_index=True)

                df_ht_away = pd.DataFrame({"Teams": teams_ht_away, "+0.5 HT Away": one_goal_ht_away}, index=None)
                df_ht_away.sort_values(by="Teams", inplace=True, ignore_index=True)

                # Unindo as informações em um único dataframe
                df_total["+1.5 Last8"] = df_last8["+1.5 Last8"]
                df_total["+1.5 Home"] = df_home["+1.5 Home"]
                df_total["+1.5 Away"] = df_away["+1.5 Away"]

                df_total["+2.5 Last8"] = df_last8["+2.5 Last8"]
                df_total["+2.5 Home"] = df_home["+2.5 Home"]
                df_total["+2.5 Away"] = df_away["+2.5 Away"]

                df_total["BTS Last8"] = df_last8["BTS Last8"]
                df_total["BTS Home"] = df_home["BTS Home"]
                df_total["BTS Away"] = df_away["BTS Away"]

                df_total["+0.5 HT Total"] = df_ht_total["+0.5 HT Total"]
                df_total["+0.5 HT Home"] = df_ht_home["+0.5 HT Home"]
                df_total["+0.5 HT Away"] = df_ht_away["+0.5 HT Away"]

                df_total.loc[len(df_total)] = ["Médias", avg_more_one_goal_total, avg_more_one_goal_last8, avg_more_one_goal_home, avg_more_one_goal_away,
                                               avg_more_two_goals_total, avg_more_two_goals_last8, avg_more_two_goals_home, avg_more_two_goals_away,
                                               avg_bts_total, avg_bts_last8, avg_bts_home, avg_bts_away,
                                               avg_one_goal_ht_total, avg_one_goal_ht_home, avg_one_goal_ht_away]

                for i in df_total.index:
                    
                    if df_total['Teams'][i] != 'Médias' and df_total['+1.5 Total'][i] >= avg_more_one_goal_total and df_total['+1.5 Last8'][i] >= avg_more_one_goal_last8:
                        
                        if df_total['+1.5 Home'][i] >= avg_more_one_goal_home:
                            mtog_teams_home.append(df_total['Teams'][i])
                        
                        if df_total['+1.5 Away'][i] >= avg_more_one_goal_away:
                            mtog_teams_away.append(df_total['Teams'][i])

                    if df_total['Teams'][i] != 'Médias' and df_total['+2.5 Total'][i] >= avg_more_two_goals_total and df_total['+2.5 Last8'][i] >= avg_more_two_goals_last8:
                        
                        if df_total['+2.5 Home'][i] >= avg_more_two_goals_home:
                            mttg_teams_home.append(df_total['Teams'][i])
                        
                        if df_total['+2.5 Away'][i] >= avg_more_two_goals_away:
                            mttg_teams_away.append(df_total['Teams'][i])

                    if df_total['Teams'][i] != 'Médias' and df_total['BTS Total'][i] >= avg_bts_total and df_total['BTS Last8'][i] >= avg_bts_last8:
                        
                        if df_total['BTS Home'][i] >= avg_bts_home:
                            bts_teams_home.append(df_total['Teams'][i])
                        
                        if df_total['BTS Away'][i] >= avg_bts_away:
                            bts_teams_away.append(df_total['Teams'][i])

                    if df_total['Teams'][i] != 'Médias' and df_total['+0.5 HT Total'][i] >= avg_one_goal_ht_total:
                        
                        if df_total['+0.5 HT Home'][i] >= avg_one_goal_ht_home:
                            oght_teams_home.append(df_total['Teams'][i])
                        
                        if df_total['+0.5 HT Away'][i] >= avg_one_goal_ht_away:
                            oght_teams_away.append(df_total['Teams'][i])
                    
                #print(f'Possibles home teams to bet in {league_name}: {mtog_teams_home}')
                #print(f'Possibles away teams to bet in {league_name}: {mtog_teams_away}')

        except:
            #print(f'{league_name} has a low number of games')
            pass
        
    # Pegando as partidas do dia
    link = latest_link + t

    if requests.get(link).status_code == 200:

        driver.get(link)
        time.sleep(2)

        try:
            driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
        except:
            #print("")
            pass

        try:
            driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
        except:
            #print("")
            pass
        
        try:
            list_of_matches = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]')
        except NoSuchElementException as e:
            try:
                list_of_matches = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]')
            except NoSuchElementException as e:
                try:
                    list_of_matches = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[3]/table[1]/tbody/tr/td/table[1]')
                except NoSuchElementException as e:
                    #print("")
                    pass

        try:
            matches = list_of_matches.find_elements(By.TAG_NAME, 'tr')
            matches.pop(0)

            date = []
            hour = []
            home = []
            away = []

            i = 2
            for match in matches:
                try:
                    date.append(match.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML'))
                    hour.append(match.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[3]/font').get_attribute('innerHTML'))
                    home.append(match.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[2]/a').get_attribute('innerHTML'))
                    away.append(match.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[4]/a').get_attribute('innerHTML'))
                except NoSuchElementException as e:
                    try:
                        date.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML'))
                        hour.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[3]/font').get_attribute('innerHTML'))
                        home.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[2]/a').get_attribute('innerHTML'))
                        away.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[4]/div[4]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[4]/a').get_attribute('innerHTML'))
                    except NoSuchElementException as e:
                        try:
                            date.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML'))
                            hour.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[3]/font').get_attribute('innerHTML'))
                            home.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[2]/a').get_attribute('innerHTML'))
                            away.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[{i}]/td[4]/a').get_attribute('innerHTML'))
                        except NoSuchElementException as e:
                            #print('')
                            pass

                i = i + 1

            i = 0
            for d in date:
                if d == 'Tu 26 Mar' and home[i] in mtog_teams_home and away[i] in mtog_teams_away:
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +1.5 gols')

                if d == 'Tu 26 Mar' and home[i] in mttg_teams_home and away[i] in mttg_teams_away:
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +2.5 gols')

                if d == 'Tu 26 Mar' and home[i] in bts_teams_home and away[i] in bts_teams_away:
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, Ambas Marcam')

                if d == 'Tu 26 Mar' and home[i] in oght_teams_home and away[i] in oght_teams_away:
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +0.5 gols HT')
                
                i = i + 1
    
        except:
            #print('')
            pass
    #driver.quit()

#while True:
#    time.sleep(1)
