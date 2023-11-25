from bs4 import BeautifulSoup
import requests
import re
import lxml

links = []


def remove_duplicates(l):
    for item in l:
        match = re.search(r"(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))


def GetLink(Keyword):
    InputText = Keyword
    source_code = requests.get('https://www.visindavefur.is/search/?q=' + InputText, timeout=12)
    soup = BeautifulSoup(source_code.content, 'lxml')
    data = []

    for link in soup.find_all('a', href=True):
        data.append(str(link.get('href')))

    flag = True

    remove_duplicates(data)
    Failat = 85
    FailNumberDone = 0
    Answer = ""
    while flag:
        try:
            for link in links:
                for j in soup.find_all('a', href=True):
                    temp = []
                    thing = str(j.get('href'))
                    FailNumberDone = FailNumberDone + 1
                    if FailNumberDone > Failat:
                        flag = False

                    if "/svar" in thing and not any(num in thing for num in ["70790", "70789", "73555", "76210"]):
                        temp.append(str(j.get('href')))
                        remove_duplicates(temp)
                        if len(Answer) == 0:
                            Answer = thing
                        flag = False

        except Exception:
            print("Villa kom upp.")
            Answer = "Villa kom upp."

    Visindia = "https://www.visindavefur.is"
    if len(Answer) == 0:
        Answer = "Fann ekkert..."
        Visindia = ""

    return (Visindia + Answer)