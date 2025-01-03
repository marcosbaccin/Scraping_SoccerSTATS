O objetivo principal desse projeto é encontrar jogos que tenham boa probabilidade de ocorrer +1.5 e/ou +2.5 gols e/ou Ambas Marcam utilizando os dados fornecidos no site https://www.soccerstats.com

O arquivo ligas.py tem como objetivo encontrar a frequência global em que ocorrem os eventos de +1.5, +2.5 gols e Ambas Marcam em partidas de diversas ligas pelo mundo.
Para isso inicialmente ele acessa a página de ligas do SoccerSTATS, em seguida coleta todos os dados referentes a +1.5, +2.5 gols e Ambas Marcam e, por fim, calcula a média geral da ocorrência desses eventos.

<div style="display: inlineblock"><br>
  <img align="center" alt="Leagues" height="400" width="800" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/01.png"><br>
  <img align="center" alt="Output_medias" height="200" width="400" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/02.png">
</div><br>

Como exemplo de saída vemos na imagem acima primeiramente um número que representa a quantidade de ligas analisadas. Logo abaixo temos as frequências de +1.5, +2.5 gols e Ambas Marcam.

Já o arquivo encontrando_jogos.py vai realizar o scraping da frequência desses eventos para cada clube. Para isso acessamos a página de cada liga e lá navegaremos por dois menus, sendo eles os menus "Goals" e "Matches".
O menu Goals apresenta os dados de gols de cada equipe da liga enquanto Matches as partidas que foram ou serão disputadas.

<div style="display: inlineblock"><br>
  <img align="center" alt="Menus" height="100" width="600" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/03.png">
</div><br>

A imagem abaixo mostra onde estão os dados que queremos extrair na página de Goals da liga. Pegaremos os dados de +1.5, +2.5 gols e Ambas Marcam de todos os clubes em todos os cenários possíveis, Total, Last 8 (últimos 8 jogos), Home (mandante) e Away (visitante).

<div style="display: inlineblock"><br>
  <img align="center" alt="Goals" height="400" width="400" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/04.png">
</div><br>

Em seguida acessamos a página de Matches da liga. Pegaremos todos os registros e salvaremos cada partida pegando a data, horário, mandante e visitante.

<div style="display: inlineblock"><br>
  <img align="center" alt="Matches" height="250" width="500" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/05.png">
</div><br>

Com todos esses dados em mãos vamos calcular quais jogos que ocorerrão no dia X (por exemplo, Sa 4 Jan) tem boas chances de ocorrer +1.5 e/ou +2.5 gols e/ou Ambas Marcam.
Para isso o algoritmo percorre a lista de jogos coletados na página de Matches e verifica quais ocorrem no dia X. Em seguida analisa os dados de gols das duas equipes envolvidas. Se ambas as equipes tem frequência de +1.5 e/ou +2.5 gols e/ou Ambas Marcam acima da média global (encontrada ao executar o arquivo ligas.py) em todos os cenários possíveis ( Total, Last 8, Home e Away) o algoritmo te informa que esse é um jogo em potencial. A imagem abaixo mostra um exemplo de saída do arquivo encontrando_jogos.py.

<div style="display: inlineblock"><br>
  <img align="center" alt="Result" height="250" width="500" src="https://github.com/marcosbaccin/soccerstats/blob/master/prints/06.png">
</div><br>

Neste exemplo, foi analisado os jogos no dia 04/01/2025 (Sa 4 Jan). Todos os jogos identificados como potencial são printados na saída e salvos em um arquivo csv.
