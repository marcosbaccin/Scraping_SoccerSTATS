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

# Estrutura padrão de link para acessar as estatísticas de gols e próximos jogos das ligas no Soccerstats
goals_link = "https://www.soccerstats.com/trends.asp?league="
matches_link = 'https://www.soccerstats.com/results.asp?league='

# Data Frame para salvar os jogos encontrados
jogos = pd.DataFrame(columns=['League', 'Date', 'Hour', 'Home', 'Away', 'Type', 'Odd'])

# Dia atual
day = 'Fr 3 Jan'

# Ligas disponíveis no Soccerstats
leagues = ['australia', 'albania',
'algeria',
'argentina',
'argentina3',
'argentina4',
'argentina5',
'argentina10',
'armenia',
'australia',
'australia2',
'australia3',
'australia4',
'australia5',
'australia6',
'australia7',
'australia8',
'australia10',
'australia11',
'australia16',
'austria',
'austria2',
'austria6',
'austria7',
'austria8',
'azerbaijan',
'bahrain',
'bangladesh',
'belarus',
'belarus2',
'belgium',
'belgium2',
'belgium3',
'belgium6',
'bolivia',
'bolivia2',
'bosnia',
'bosnia2',
'brazil',
'brazil2',
'brazil3',
'brazil4',
'brazil5',
'brazil6',
'brazil7',
'brazil8',
'brazil9',
'brazil11',
'brazil12',
'brazil14',
'brazil15',
'brazil16',
'brazil17',
'brazil18',
'brazil19',
'brazil20',
'brazil21',
'bulgaria',
'bulgaria2',
'canada',
'chile',
'chile2',
'china',
'china2',
'china3',
'colombia',
'colombia2',
'costarica',
'costarica2',
'croatia',
'croatia2',
'cyprus',
'cyprus2',
'czechrepublic',
'czechrepublic2',
'czechrepublic3',
'czechrepublic4',
'denmark',
'denmark2',
'denmark3',
'ecuador',
'ecuador2',
'ecuador3',
'egypt',
'england',
'england2',
'england3',
'england4',
'england5',
'england6',
'england7',
'england8',
'england9',
'england10',
'england11',
'england15',
'england17',
'england18',
'england19',
'estonia',
'estonia2',
'estonia3',
'ethiopia',
'faroeislands',
'faroeislands2',
'finland',
'finland2',
'finland3',
'finland4',
'finland5',
'finland6',
'finland7',
'france',
'france2',
'france3',
'france4',
'france5',
'france6',
'france14',
'georgia',
'georgia2',
'georgia3',
'germany',
'germany2',
'germany3',
'germany4',
'germany5',
'germany6',
'germany7',
'germany8',
'germany9',
'germany10',
'germany11',
'germany12',
'germany15',
'germany16',
'germany17',
'germany18',
'germany19',
'germany20',
'germany21',
'germany22',
'germany23',
'germany24',
'ghana',
'gibraltar',
'greece',
'guatemala',
'guatemala2',
'honduras',
'honduras2',
'hongkong',
'hungary',
'hungary2',
'iceland',
'iceland2',
'iceland3',
'iceland4',
'iceland5',
'iceland6',
'india',
'india2',
'indonesia',
'iran',
'iraq',
'ireland',
'ireland2',
'ireland3',
'israel',
'israel2',
'israel3',
'israel4',
'italy',
'italy2',
'italy3',
'italy4',
'italy5',
'italy6',
'italy7',
'italy8',
'italy9',
'italy10',
'italy11',
'italy12',
'italy13',
'italy14',
'italy15',
'italy16',
'italy17',
'jamaica',
'japan',
'japan2',
'japan3',
'japan4',
'japan5',
'jordan',
'kazakhstan',
'kosovo',
'kuwait',
'latvia',
'latvia2',
'lithuania',
'lithuania2',
'luxembourg',
'malaysia',
'malta',
'malta2',
'mauritius',
'mexico',
'mexico2',
'mexico3',
'moldova',
'mongolia',
'montenegro',
'morocco',
'morocco2',
'myanmar',
'netherlands',
'netherlands2',
'netherlands3',
'netherlands4',
'netherlands6',
'nicaragua',
'nicaragua2',
'northernireland',
'northernireland2',
'northernireland3',
'northmacedonia',
'norway',
'norway2',
'norway3',
'norway4',
'norway5',
'norway6',
'norway7',
'norway8',
'norway9',
'norway10',
'norway11',
'norway12',
'oman',
'panama',
'panama2',
'paraguay',
'paraguay2',
'paraguay3',
'peru',
'peru2',
'philippines',
'poland',
'poland2',
'poland3',
'poland4',
'portugal',
'portugal2',
'portugal4',
'portugal5',
'portugal6',
'portugal7',
'portugal8',
'qatar',
'qatar2',
'romania',
'romania2',
'russia',
'russia2',
'rwanda',
'sanmarino',
'saudiarabia',
'saudiarabia2',
'scotland',
'scotland2',
'scotland3',
'scotland4',
'scotland7',
'serbia',
'serbia2',
'singapore',
'slovakia',
'slovakia2',
'slovakia3',
'slovenia',
'southafrica',
'southafrica2',
'southkorea',
'southkorea2',
'southkorea3',
'southkorea4',
'spain',
'spain2',
'spain3',
'spain4',
'spain5',
'spain6',
'spain7',
'spain8',
'spain9',
'spain10',
'spain11',
'spain12',
'spain13',
'spain14',
'spain15',
'spain16',
'spain17',
'spain18',
'spain19',
'sweden',
'sweden2',
'sweden3',
'sweden4',
'sweden5',
'sweden6',
'sweden7',
'sweden8',
'sweden9',
'sweden10',
'sweden11',
'sweden12',
'switzerland',
'switzerland2',
'switzerland3',
'switzerland4',
'tajikistan',
'thailand',
'thailand2',
'turkey',
'turkey2',
'turkey3',
'turkey4',
'turkey5',
'turkey6',
'turkey7',
'turkey8',
'uae',
'uganda',
'ukraine',
'uruguay',
'uruguay2',
'uruguay3',
'usa',
'usa2',
'usa3',
'usa5',
'usa6',
'usa7',
'uzbekistan',
'venezuela',
'vietnam',
'vietnam2',
'vietnam3',
'wales',
'zambia',
'zimbabwe', 'australia',]

"""
teste = ['brazil', 'spain', 'france', 'australia', 'australia2', 'bangladesh', 'cyprus', 'scotland2', 'ethiopia', 'france2',
         'ghana', 'iraq', 'israel2', 'israel3', 'israel4', 'india', 'morocco', 'wales', 'portugal', 'turkey',
         'turkey2', 'uganda', 'brazil',]


leagues_mtog = []

leagues_mttg = []

leagues_three = []

leagues_bts = []
"""

for t in leagues:
    
    # Criando o link da página de gols da liga (t)
    link = goals_link + t

    #mtog_teams_total = {}
    #mtog_teams_last8 = {}
    mtog_teams_home = {} # mtog (more than one goal)
    mtog_teams_away = {}

    #mttg_teams_total = {}
    #mttg_teams_last8 = {}
    mttg_teams_home = {} # mttg (more than two goals)
    mttg_teams_away = {}

    #three_teams_total = {}
    #three_teams_last8 = {}
    three_teams_home = {} # more than three goals
    three_teams_away = {}

    #bts_teams_total = {}
    #bts_teams_last8 = {}
    bts_teams_home = {} # more than three goals
    bts_teams_away = {}

    #if t in leagues_mttg or t in leagues_three or t in leagues_bts:

    # Verifica se a resposta da requisição para o link fornecido é bem-sucedida (status code 200)
    if requests.get(link).status_code == 200:

        driver.get(link)
        #time.sleep(1)

        try:
            # Clicar em aceitar os cookies da página
            driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
        except:
            #print("")
            pass

        try:
            # Fecha anúncios
            driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
        except:
            #print("")
            pass
        
        # Pega o nome da liga
        try:
            league_name = driver.find_element(By.XPATH, '/html/head/title').get_attribute('innerHTML').replace(' - goal statistics, over under stats and total goals', '')
        except NoSuchElementException as e:
            league_name = t

        try:
            
            # Pega a tabela onde se encontra os dados de gols no total
            try:
                total_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table')
            except NoSuchElementException as e:
                try:
                    total_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/table')
                except NoSuchElementException as e:
                    total_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table')

            teams_total = []
            more_one_goal_total = []
            more_two_goals_total = []
            #more_three_goals_total = []
            bts_total = []
            
            # Cria uma lista composta por cada linha da tabela de gols como mandante
            total_goals_stats_teams = total_goals_stats.find_elements(By.CLASS_NAME, "odd")

            i = 1
            for item in total_goals_stats_teams:
                # Pega o nome do time
                teams_total.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                
                # Pega os dados de +1.5, +2.5 e +3.5 gols como mandante do time
                try:
                    more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                    more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                    #more_three_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                    bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                except NoSuchElementException as e:
                    try:
                        more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        more_one_goal_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_total.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[1]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                i = i + 1

            # Pega a tabela onde se encontra os dados de gols nos últimos 8 jogos
            try:
                last8_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table')
            except NoSuchElementException as e:
                try:
                    last8_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[2]/table')
                except NoSuchElementException as e:
                    last8_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table')

            teams_last8 = []
            more_one_goal_last8 = []
            more_two_goals_last8 = []
            #more_three_goals_last8 = []
            bts_last8 = []
            
            # Cria uma lista composta por cada linha da tabela de gols como mandante
            last8_goals_stats_teams = last8_goals_stats.find_elements(By.CLASS_NAME, "odd")

            i = 1
            for item in last8_goals_stats_teams:
                # Pega o nome do time
                teams_last8.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                
                # Pega os dados de +1.5, +2.5 e +3.5 gols como mandante do time
                try:
                    more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                    more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                    #more_three_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                    bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                except NoSuchElementException as e:
                    try:
                        more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        more_one_goal_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_last8.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                i = i + 1
            
            # Pega a tabela onde se encontra os dados de gols como mandante
            try:
                home_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table')
            except NoSuchElementException as e:
                try:
                    home_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[3]/table')
                except NoSuchElementException as e:
                    home_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table')

            teams_home = []
            more_one_goal_home = []
            more_two_goals_home = []
            #more_three_goals_home = []
            bts_home = []
            
            # Cria uma lista composta por cada linha da tabela de gols como mandante
            home_goals_stats_teams = home_goals_stats.find_elements(By.CLASS_NAME, "odd")

            i = 1
            for item in home_goals_stats_teams:
                # Pega o nome do time
                teams_home.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                
                # Pega os dados de +1.5, +2.5 e +3.5 gols como mandante do time
                try:
                    more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                    more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                    #more_three_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                    bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                except NoSuchElementException as e:
                    try:
                        more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        more_one_goal_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_home.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                i = i + 1

            # Pega a tabela onde se encontra os dados de gols como visitante
            try:
                away_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table')
            except NoSuchElementException as e:
                try:
                    away_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[4]/table')
                except NoSuchElementException as e:
                    away_goals_stats = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table')

            teams_away = []
            more_one_goal_away = []
            more_two_goals_away = []
            #more_three_goals_away = []
            bts_away = []
            
            # Cria uma lista composta por cada linha da tabela de gols como visitante
            away_goals_stats_teams = away_goals_stats.find_elements(By.CLASS_NAME, "odd")

            i = 1
            for item in away_goals_stats_teams:
                # Pega o nome do time
                teams_away.append(item.find_element(By.TAG_NAME, "a").get_attribute("innerHTML"))
                
                # Pega os dados de +1.5, +2.5 e +3.5 gols como visitante do time
                try:
                    more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                    more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                    #more_three_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                    bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                except NoSuchElementException as e:
                    try:
                        more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))
                    except NoSuchElementException as e:
                        more_one_goal_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[5]').get_attribute("sorttable_customkey")))
                        more_two_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[6]').get_attribute("sorttable_customkey")))
                        #more_three_goals_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[7]').get_attribute("sorttable_customkey")))
                        bts_away.append(float(item.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{i}]/td[10]').get_attribute("sorttable_customkey")))

                i = i + 1
            
            # Salvando os dados em dataframes
            df_total = pd.DataFrame({"Teams Total": teams_total, "+1.5 Total": more_one_goal_total,
                                     "+2.5 Total": more_two_goals_total, "BTS Total": bts_total}, index=None)
            df_total.sort_values(by="Teams Total", inplace=True, ignore_index=True)

            df_last8 = pd.DataFrame({"Teams Last8": teams_last8, "+1.5 Last8": more_one_goal_last8,
                                     "+2.5 Last8": more_two_goals_last8, "BTS Last8": bts_last8}, index=None)
            df_last8.sort_values(by="Teams Last8", inplace=True, ignore_index=True)

            df_home = pd.DataFrame({"Teams Home": teams_home, "+1.5 Home": more_one_goal_home,
                                    "+2.5 Home": more_two_goals_home, "BTS Home": bts_home}, index=None)
            df_home.sort_values(by="Teams Home", inplace=True, ignore_index=True)

            df_away = pd.DataFrame({"Teams Away": teams_away, "+1.5 Away": more_one_goal_away,
                                    "+2.5 Away": more_two_goals_away, "BTS Away": bts_away}, index=None)
            df_away.sort_values(by="Teams Away", inplace=True, ignore_index=True)

            # Unindo as informações em um único dataframe
            df_total["+1.5 Last8"] = df_last8["+1.5 Last8"]
            df_total["+2.5 Last8"] = df_last8["+2.5 Last8"]
            #df_total["+3.5 Last8"] = df_last8["+3.5 Last8"]
            df_total["BTS Last8"] = df_last8["BTS Last8"]

            df_total["+1.5 Home"] = df_home["+1.5 Home"]
            df_total["+2.5 Home"] = df_home["+2.5 Home"]
            #df_total["+3.5 Home"] = df_home["+3.5 Home"]
            df_total["BTS Home"] = df_home["BTS Home"]
            
            df_total["+1.5 Away"] = df_away["+1.5 Away"]
            df_total["+2.5 Away"] = df_away["+2.5 Away"]
            #df_total["+3.5 Away"] = df_away["+3.5 Away"]
            df_total["BTS Away"] = df_away["BTS Away"]

            #print(df_total)

            for i in df_total.index:
                
                # Verifica se o time está acima da chance de +1.5 gols como mandante
                if df_total['+1.5 Total'][i] > 74 and df_total['+1.5 Last8'][i] > 74:
                    if df_total['+1.5 Home'][i] > 74:
                        mtog_teams_home[df_total['Teams Total'][i]] = (df_total['+1.5 Total'][i] + df_total['+1.5 Last8'][i] + df_total['+1.5 Home'][i]) / 3
                        #mtog_teams_home.append(df_total['Teams'][i])
                    
                    if df_total['+1.5 Away'][i] > 74:
                        mtog_teams_away[df_total['Teams Total'][i]] = (df_total['+1.5 Total'][i] + df_total['+1.5 Last8'][i] + df_total['+1.5 Away'][i]) / 3
                        #mtog_teams_away.append(df_total['Teams'][i])
                
                if df_total['+2.5 Total'][i] > 52 and df_total['+2.5 Last8'][i] > 52:
                    if df_total['+2.5 Home'][i] > 52:
                        mttg_teams_home[df_total['Teams Total'][i]] = (df_total['+2.5 Total'][i] + df_total['+2.5 Last8'][i] + df_total['+2.5 Home'][i]) / 3
                        #mttg_teams_home.append(df_total['Teams'][i])
                    
                    if df_total['+2.5 Away'][i] > 52:
                        mttg_teams_away[df_total['Teams Total'][i]] = (df_total['+2.5 Total'][i] + df_total['+2.5 Last8'][i] + df_total['+2.5 Away'][i]) / 3
                        #mttg_teams_away.append(df_total['Teams'][i])
                """
                if t in leagues_three and df_total['+3.5 Total'][i] > 31 and df_total['+3.5 Last8'][i] > 31:
                    if df_total['+3.5 Home'][i] > 31:
                        three_teams_home[df_total['Teams Total'][i]] = (df_total['+3.5 Total'][i] + df_total['+3.5 Last8'][i] + df_total['+3.5 Home'][i]) / 3
                        #three_teams_home.append(df_total['Teams'][i])
                    
                    if df_total['+3.5 Away'][i] > 31:
                        three_teams_away[df_total['Teams Total'][i]] = (df_total['+3.5 Total'][i] + df_total['+3.5 Last8'][i] + df_total['+3.5 Away'][i]) / 3
                        #three_teams_away.append(df_total['Teams'][i])
                """
                if df_total['BTS Total'][i] > 51 and df_total['BTS Last8'][i] > 51:
                    if df_total['BTS Home'][i] > 51:
                        bts_teams_home[df_total['Teams Total'][i]] = (df_total['BTS Total'][i] + df_total['BTS Last8'][i] + df_total['BTS Home'][i]) / 3
                        #bts_teams_home.append(df_total['Teams'][i])
                    
                    if df_total['BTS Away'][i] > 51:
                        bts_teams_away[df_total['Teams Total'][i]] = (df_total['BTS Total'][i] + df_total['BTS Last8'][i] + df_total['BTS Away'][i]) / 3
                        #bts_teams_away.append(df_total['Teams'][i])

        except:
            #print(f'{league_name} has a low number of games')
            pass


    # Pegando as partidas do dia
    link = matches_link + t

    # Verifica se a resposta da requisição para o link fornecido é bem-sucedida (status code 200)
    if requests.get(link).status_code == 200:

        driver.get(link)
        #time.sleep(1)

        # Clicar em aceitar os cookies da página
        try:
            driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
        except:
            #print("")
            pass

        # Fecha anúncios
        try:
            #driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
            driver.find_element(By.CSS_SELECTOR, '#dismiss-button > div > span').click()
        except:
            #print("")
            pass
        
        # Pega a tabela onde se encontra as próximas partidas
        try:
            list_of_matches = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[6]/table[1]')
        except NoSuchElementException as e:
            try:
                list_of_matches = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[7]/table[1]')
            except NoSuchElementException as e:
                pass
        try:
            # Cria uma lista composta por cada linha da tabela dos próximos jogos
            matches = list_of_matches.find_elements(By.TAG_NAME, 'tr')
            # Remove o cabeçalho
            #matches.pop(0)

            date = []
            hour = []
            home = []
            away = []

            i = 3
            for match in matches:
                # Pega os dados de data, hora, mandante e visitante da partida
                try:
                    data = match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[6]/table[1]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML')
                    if data == day:
                        date.append(data)
                        try:
                            hour.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[6]/table[1]/tbody/tr[{i}]/td[3]/font').get_attribute('innerHTML'))
                        except NoSuchElementException as e:
                            hour.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[6]/table[1]/tbody/tr[{i}]/td[3]').get_attribute('innerHTML'))
                        home.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[6]/table[1]/tbody/tr[{i}]/td[2]').get_attribute('innerHTML').replace('&nbsp;', ''))
                        away.append(match.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div[2]/div[6]/table[1]/tbody/tr[{i}]/td[4]').get_attribute('innerHTML').replace('&nbsp;', ''))
                except NoSuchElementException as e:
                    try:
                        data = match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[7]/table[1]/tbody/tr[{i}]/td[1]/font').get_attribute('innerHTML')
                        if data == day:
                            date.append(data)
                            hour.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[7]/table[1]/tbody/tr[{i}]/td[3]/font').get_attribute('innerHTML'))
                            home.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[7]/table[1]/tbody/tr[{i}]/td[2]').get_attribute('innerHTML').replace('&nbsp;', ''))
                            away.append(match.find_element(By.XPATH, f'/html/body/div[4]/div/div[2]/div[7]/table[1]/tbody/tr[{i}]/td[4]').get_attribute('innerHTML').replace('&nbsp;', ''))
                    except NoSuchElementException as e:
                        pass

                i = i + 1

            i = 0
            for d in date:
                # Verifica se no dia atual o mandante e o visitante estão entre os times acima das chances para +1.5 gols
                if d == day and home[i] in mtog_teams_home and away[i] in mtog_teams_away:
                    odd = 100 / ((mtog_teams_home.get(home[i]) + mtog_teams_away.get(away[i])) / 2)
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +1.5 gols, -> {odd:.2f}')
                    
                    # Salva o jogo no Data Frame
                    jogos.loc[len(jogos)] = [league_name, d, hour[i], home[i], away[i], '+1.5 gols', f' -> {odd:.2f}']
                
                # Verifica se no dia atual o mandante e o visitante estão entre os times acima das chances para +2.5 gols
                if d == day and home[i] in mttg_teams_home and away[i] in mttg_teams_away:
                    odd = 100 / ((mttg_teams_home.get(home[i]) + mttg_teams_away.get(away[i])) / 2)
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +2.5 gols, -> {odd:.2f}')
                    
                    # Salva o jogo no Data Frame
                    jogos.loc[len(jogos)] = [league_name, d, hour[i], home[i], away[i], '+2.5 gols', f' -> {odd:.2f}']
                """
                # Verifica se no dia atual o mandante e o visitante estão entre os times acima das chances para +3.5 gols
                if d == day and home[i] in three_teams_home and away[i] in three_teams_away:
                    odd = 100 / ((three_teams_home.get(home[i]) + three_teams_away.get(away[i])) / 2)
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, +3.5 gols, -> {odd:.2f}')
                    
                    # Salva o jogo no Data Frame
                    jogos.loc[len(jogos)] = [league_name, d, hour[i], home[i], away[i], '+3.5 gols', f' -> {odd:.2f}']
                """
                # Verifica se no dia atual o mandante e o visitante estão entre os times acima das chances para BTS
                if d == day and home[i] in bts_teams_home and away[i] in bts_teams_away:
                    odd = 100 / ((bts_teams_home.get(home[i]) + bts_teams_away.get(away[i])) / 2)
                    print(f'{league_name}, {d}, {hour[i]}, {home[i]} x {away[i]}, BTS, -> {odd:.2f}')
                    
                    # Salva o jogo no Data Frame
                    jogos.loc[len(jogos)] = [league_name, d, hour[i], home[i], away[i], 'BTS', f' -> {odd:.2f}']
                
                i = i + 1
    
        except:
            #print('')
            pass

# Ordena os dados pelo tipo do mercado e hora e salva em um csv
jogos.sort_values(['Type', 'Hour'], ascending=[True, True], inplace=True)
jogos.to_csv("C:/VScode_projects/soccerstats/jogos.csv", index=False)
