import datetime
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
    configTemplate = {"server": 947666187653885982, "user": 722452978870779934, "clears": True}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)


#get var from the external file
server = configData["server"]
user = configData["user"]
clears = configData["clears"]

#vars ecc
_stats = Table(title="Stats")
console = Console()
url = "https://unbelievaboat.com/api/v1/guilds/{}/users/{}".format(server, user)
headers = {"Accept": "application/json", "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDA3MzUxNjY4Njk5OTU3MDExIiwiaWF0IjoxNjYwMjQxNzU5fQ.7z4GDeAH3hTUoMvFDj-1THOooNSmSUos5qDOfIEcoKU"}


#stats table
_stats.add_column("Clock")
_stats.add_column("Hand")
_stats.add_column("Bank")
_stats.add_column("Total")
_stats.add_column("Money Made")
_stats.add_column("Rank")


#get api info
def get_stats():
    response = requests.get(url, headers=headers)
    y = json.loads(response.text)
    # set variables
    global rank, cash, bank, total
    rank = y["rank"]
    cash = y["cash"]
    bank = y["bank"]
    total = y["total"]


#sets initial money
get_stats()
initial_money = total

#loop
while(True):

  if clears == True: #resets the label
    
    _stats = Table(title="Stats")
    _stats.add_column("Clock")
    _stats.add_column("Hand")
    _stats.add_column("Bank")
    _stats.add_column("Total")
    _stats.add_column("Money Made")
    _stats.add_column("Rank")


  #clear
  os.system('cls' if os.name == 'nt' else 'clear')

  #update stats
  get_stats()
  made_money = total - initial_money

  #update label
  _stats.add_row(datetime.datetime.now().strftime("%H:%M:%S"), 
                  "{}$".format(f"{cash:,}"), 
                  "{}$".format(f"{bank:,}"), 
                  "{}$".format(f"{total:,}"), 
                  "{}$".format(f"{made_money:,}"), 
                  "#{}".format(rank)
                )

  console.print(_stats)

  time.sleep(10)