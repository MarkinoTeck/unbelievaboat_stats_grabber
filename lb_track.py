from rich.console import Console
from rich.table import Table
import time
import json
import requests
import os


# generate or get confing file
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"server": 947666187653885982, "clears": True}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)


#get var from the external file
server = configData["server"]


#vars ecc
_top = Table(title="Top 10")
console = Console()
url = "https://unbelievaboat.com/api/v1/guilds/{}/users/?sort=total&limit=30&page=1".format(server)
headers = {"Accept": "application/json", "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDA3MzUxNjY4Njk5OTU3MDExIiwiaWF0IjoxNjYwMjQxNzU5fQ.7z4GDeAH3hTUoMvFDj-1THOooNSmSUos5qDOfIEcoKU"}


#get api info
def get_top():
    response = requests.get(url, headers=headers)
    global y
    y = json.loads(response.text)


#sets initial money
get_top()


#loop
while(True):

  #reset
  _top = Table(title="Top 30")
  _top.add_column("Rank")
  _top.add_column("Name")
  _top.add_column("Total", style="light_green")

  #clear
  os.system('cls' if os.name == 'nt' else 'clear')
  time.sleep(0.2)

  #update stats
  get_top()

  #update label
  for pearson in y['users']:
    _top.add_row("#{}".format(pearson['rank']),
                   "{}".format(pearson['user_id']),
                   "{}".format(f"{pearson['total']:,}")
                  )

  console.print(_top)

  time.sleep(10)