from typing import Dict
import requests
import re
import json
import time

count = 0

def search(keywords: str, max_results=1) -> Dict:
    url = 'https://duckduckgo.com/'
    params = {
    	'q': keywords
    }

    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I)

    if not searchObj:
        return -1


    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */* q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,enq=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '1'),
        ('v7exp', 'a'),
    )

    requestUrl = url + "i.js"

    while True:
      while True:
        try:
            res = requests.get(requestUrl, headers=headers, params=params)
            data = json.loads(res.text)
            break
        except ValueError:
            time.sleep(5)
            continue

      thing = printJson(data["results"])

      if len(data["results"]) < 150:
        return thing

      if len(data["results"]) > 145:
        return None
        
      requestUrl = url + data["next"]

      
      time.sleep(1)
      break

  

bannedSites = ["Pornhub.com","Kink.com","YouJizz.com","Redtube.com","8Tube.xxx","Match.com","MeetMe.com","OKCupid.com","Tinder.com","Bumble.com","Chaturbate.com","Bongacams.com","MyFreeCams.com","LiveJasmin.com","SlutRoulette.com","ratemypoo.com","ratemypoo.me","sex","Sex","poo","Poo","https://preview.redd.it/hghhgabyokq21.jpg?auto=webp&s=432754e85c4ac90c29d6ad22916e537a7b12a9d6","drugs","Drugs"]
#Síður sem eru ekki leyfðar

def printJson(objs):
    for obj in objs:
      print("__________")
      print("Breidd {0}, Hæð {1}".format(obj["width"], obj["height"]))
      print("Smámynd {0}".format(obj["thumbnail"]))
      print("Vefsvæði {0}".format(obj["url"]))
      print("Titill {0}".format(obj["title"].encode('utf-8')))
      print("Mynd {0}".format(obj["image"]))
      print("__________")
      

      if any(word in str(obj["image"]) for word in bannedSites):
        return "Má ekki sýna það. Það er bannað..."

        
      return str(obj["image"])
      
      break
