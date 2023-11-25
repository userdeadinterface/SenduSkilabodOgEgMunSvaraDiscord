import time
import requests
from bs4 import BeautifulSoup
import random
import datetime
import os
import xml.etree.ElementTree as ET
import datetime

def saekjafrettirXMLGeymsla(merkja):
  url = "https://www.ruv.is/rss/frettir"
  response = requests.get(url)

  if not os.path.exists("Skrar"):
      os.mkdir("Skrar")

  filename = "Skrar/frettir.xml"
  if merkja == True:
    nunaidag = datetime.datetime.today().strftime('%Y-%m-%d_%H:%M')
    filename = f"Skrar/frettir{nunaidag}.xml"
    
  with open(filename, "wb") as f:
    f.write(response.content)

  tree = ET.parse(filename)
  root = tree.getroot()

  listiyfirtengla = []
  for item in root.findall("./channel/item"):
      link = item.find("link").text
      listiyfirtengla.append(link)

  return(listiyfirtengla)

def saekjafrettirXML():
  url = "https://www.ruv.is/rss/frettir"
  response = requests.get(url)

  root = ET.fromstring(response.content)

  listiyfirtengla = []
  for item in root.findall("./channel/item"):
    link = item.find("link").text
    listiyfirtengla.append(link)

  return(listiyfirtengla)