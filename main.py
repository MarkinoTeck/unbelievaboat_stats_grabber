from rich.console import Console
from rich.table import Table
import time
import json
import requests
import os

my_stats = Table(title="Stats")
console = Console()
# collect all pets url
url = "https://unbelievaboat.com/api/v1/guilds/947666187653885982/users/722452978870779934"
headers = {"Accept": "application/json", "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDA1MDk2ODQ3NjU3Nzk4MzkzIiwiaWF0IjoxNjU5NzA0MTYyfQ.bfTtQZcF0LEHiGqPaJJbVR8uONihcUf5KvDjo9XJy2w"}



#stats
my_stats.add_column("Hand")
my_stats.add_column("Bank")
my_stats.add_column("Total")
my_stats.add_column("Money Made")
my_stats.add_column("Rank")
my_stats.add_column("Betting")
my_stats.add_column("Bet Color")
my_stats.add_column("Starting Bet")



# get api info
def get_stats():
    response = requests.get(url, headers=headers)
    y = json.loads(response.text)
    # set variables
    global rank, cash, bank, total
    rank = y["rank"]
    cash = y["cash"]
    bank = y["bank"]
    total = y["total"]


# scegli bet iniziale
get_stats()
initial_money = total



def main_():
 while(True):
  #clear
  os.system('cls' if os.name == 'nt' else 'clear')


  #update stats
  get_stats()
  global made_money, rank
  made_money = total - initial_money

  #update label

  my_stats.add_row("{}$".format(f"{cash:,}"), "{}$".format(f"{bank:,}"), "{}$".format(f"{total:,}"), "{}$".format(f"{made_money:,}"), "#{}".format(rank))


  console.print(my_stats)

  time.sleep(30)


# loops
main_()
