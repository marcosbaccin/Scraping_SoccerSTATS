# Importação das bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

# Importando e inicializando o driver do Chrome
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Estrutura padrão de link para acessar as estatísticas de gols das ligas no Soccerstats
standard_link = "https://www.soccerstats.com/trends.asp?league="

# Ligas que possuem estatísticas de 1º tempo
leagues = ['albania', 
           'algeria',
           'algeria3',
           'andorra', 
           'argentina', 
           'argentina2', 
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
           'belarus4', 
           'belgium', 
           'belgium2', 
           'belgium3', 
           'belgium4', 
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
           'brazil10', 
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
           'chile3', 
           'china', 
           'china2', 
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
           'ethiopia',
           'faroeislands',
           'faroeislands2', 
           'finland',
           'finland2',
           'finland3', 
           'finland4', 
           'finland5',
           'finland6',
           'france', 
           'france2',
           'france3',
           'france4', 
           'france5',
           'france6',
           'france7', 
           'france14',
           'georgia', 
           'georgia2',
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
           'greece2',
           'greece3', 
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
           'ivorycoast', 
           'jamaica',
           'japan', 
           'japan2',
           'japan3', 
           'japan4', 
           'japan5',
           'jordan', 
           'kazakhstan',
           'kenya',
           'kosovo', 
           'kuwait',
           'latvia', 
           'latvia2',
           'lithuania',
           'lithuania2',
           'luxembourg',
           'malaysia',
           'malaysia2',
           'malta', 
           'malta2',
           'mauritius', 
           'mexico',
           'mexico2',
           'mexico5', 
           'mexico6',
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
           'newzealand', 
           'nicaragua', 
           'nicaragua2', 
           'nigeria',
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
           'peru3', 
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
           'switzerland4',
           'syria',
           'tajikistan',
           'tanzania',
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
           'turkey10',
           'uae', 
           'uae2', 
           'uganda',
           'ukraine', 
           'ukraine2', 
           'uruguay',
           'uruguay2',
           'uruguay3',
           'usa', 
           'usa2',
           'usa3',
           'usa5', 
           'uzbekistan',
           'venezuela',
           'vietnam',
           'vietnam2',
           'vietnam3',
           'wales', 
           'zambia', 
           'zimbabwe']

# Input do usuario para a escolha da liga
print("Leagues:")

for league in leagues:
    print(f"({leagues.index(league)}) {league}")

league = int(input("Choose a league: "))

# Montando o link para acessar a página da liga
link = standard_link + leagues[league]
print(link)

# Acessando a página da liga
driver.get(link)
time.sleep(5)

# Fechando o anúncio caso apareça
try:
    driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
except:
    print("Sem anúncio")

Teams_home_ht = []
One_goal_ht_home = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de gols no 1º tempo)
teams_home_ht = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr")
if len(teams_home_ht) == 0:
    teams_home_ht = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr")

# Pegando as informações
index_gh = 1
for team_h_ht in teams_home_ht:
    t = team_h_ht.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        g = team_h_ht.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr[{index_gh}]/td[4]/span").get_attribute("innerHTML")
    except:
        g = team_h_ht.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[{index_gh}]/td[4]/span").get_attribute("innerHTML")

    index_gh += 1
    g = int(g.replace("%", ""))
    Teams_home_ht.append(t)
    One_goal_ht_home.append(g)

# print(Teams_home)
# print(len(Teams_home))
# print(One_goal_ht_home)
# print(len(One_goal_ht_home))

Teams_away_ht = []
One_goal_ht_away = []

teams_away_ht = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr")
if len(teams_away_ht) == 0:
    teams_away_ht = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tbody/tr")

index_gw = 1
for team_a_ht in teams_away_ht:
    t = team_a_ht.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        g = team_a_ht.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr[{index_gw}]/td[4]/span").get_attribute("innerHTML")
    except:
        g = team_a_ht.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tbody/tr[{index_gw}]/td[4]/span").get_attribute("innerHTML")

    index_gw += 1
    g = int(g.replace("%", ""))
    Teams_away_ht.append(t)
    One_goal_ht_away.append(g)

# print(Teams_away)
# print(len(Teams_away))
# print(One_goal_ht_away)
# print(len(One_goal_ht_away))

Teams_home = []
More_2_goals_home = []
Both_teams_to_score_home = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de jogos com +2.5 gols e BTTS)
teams_home = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr")
if len(teams_home) == 0:
    teams_home = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr")

# Pegando as informações
index_gh = 1
for team_h in teams_home:
    t = team_h.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        m2g = team_h.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[6]/font/span").get_attribute("innerHTML")
    except:
        m2g = team_h.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[6]/font/span").get_attribute("innerHTML")

    try:
        btts = team_h.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[10]/span").get_attribute("innerHTML")
    except:
        btts = team_h.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[10]/span").get_attribute("innerHTML")

    index_gh += 1
    m2g = int(m2g.replace("%", ""))
    btts = int(btts.replace("%", ""))
    Teams_home.append(t)
    More_2_goals_home.append(m2g)
    Both_teams_to_score_home.append(btts)

Teams_away = []
More_2_goals_away = []
Both_teams_to_score_away = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de jogos com +2.5 gols e BTTS)
teams_away = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr")
if len(teams_away) == 0:
    teams_away = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr")

# Pegando as informações
index_ga = 1
for team_a in teams_away:
    t = team_a.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        m2g = team_a.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[6]/font/span").get_attribute("innerHTML")
    except:
        m2g = team_a.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[6]/font/span").get_attribute("innerHTML")

    try:
        btts = team_a.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[10]/span").get_attribute("innerHTML")
    except:
        btts = team_a.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[10]/span").get_attribute("innerHTML")

    index_ga += 1
    m2g = int(m2g.replace("%", ""))
    btts = int(btts.replace("%", ""))
    Teams_away.append(t)
    More_2_goals_away.append(m2g)
    Both_teams_to_score_away.append(btts)

# Salvando as informações em um dataframe
df_h = pd.DataFrame({"Team Home": Teams_home_ht, "One Goal HT home": One_goal_ht_home}, index=None)
df_h.sort_values(by="Team Home", inplace=True, ignore_index=True)
# print(df_h)

# Organizando as informações
df_a = pd.DataFrame({"Team Away": Teams_away_ht, "One Goal HT away": One_goal_ht_away}, index=None)
df_a.sort_values(by="Team Away", inplace=True, ignore_index=True)
# print(df_a)

df_h2 = pd.DataFrame({"Team Home": Teams_home, "More 2 Goals home": More_2_goals_home, "Btts home": Both_teams_to_score_home}, index=None)
df_h2.sort_values(by="Team Home", inplace=True, ignore_index=True)

df_a2 = pd.DataFrame({"Team Away": Teams_away, "More 2 Goals away": More_2_goals_away, "Btts away": Both_teams_to_score_away}, index=None)
df_a2.sort_values(by="Team Away", inplace=True, ignore_index=True)

df_h["One Goal HT away"] = df_a["One Goal HT away"]
df_h["More 2 Goals home"] = df_h2["More 2 Goals home"]
df_h["Btts home"] = df_h2["Btts home"]
df_h["More 2 Goals away"] = df_a2["More 2 Goals away"]
df_h["Btts away"] = df_a2["Btts away"]
print(df_h)

# Salvando os dados coletados em uma planilha
df_h.to_excel(f"Goals_stats_{leagues[league]}.xlsx", index=False)
