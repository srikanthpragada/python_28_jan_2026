
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.tiobe.com/tiobe-index")
if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find( id = "top20")
body = table.tbody

rows = body.find_all("tr")

for row in rows[:10]:
    cols = row.find_all("td")
    lang = cols[4].text
    rank = cols[5].text
    print(f"{lang:20}  {rank}")
