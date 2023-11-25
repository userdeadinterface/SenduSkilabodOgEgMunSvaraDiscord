#ATH: Þetta er ekki upprunalegi kóðinn heldur breytt útgáfa af honum, en inniheldur samt ennþá gamlan kóða

##Import##
import os
import discord
import random
import time
import requests
import re
import bs4
import urllib.request
from covid import Covid
import asyncio
import ruv
from reynir_correct import check_errors
covid = Covid()

import pip
from datetime import datetime


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

from googletrans import Translator #ATH: Notið googletrans==3.1.0a0
Translate = Translator()

all_words = [
    "Fokk", "Grettir", "Shit", "Refur", "Fox", "Lol", "!Villuleita", "!Hjalp",
    "!Manuð", "!Lastupdate", "Mamma", "Gucci", "69", "!Orð", "!Nafnalisti",
    "Haltu Kjafti", "Þegiðu", "Ok", "Ókei", "Já", "Nei", "Ekkert",
    "Sendi Skilaboð"
]#Aukaorð

gretting_words = [
    "Hæ", "Sæl", "Góðan Dag", "Halló", "Hallo", "Gleðileg"
]

##########
#Ljót Orð#
bad_words = []

with open("bonnudord.txt",encoding="utf-8") as fileobj:
  it = iter(fileobj)
  # Settings
  TitleWords = True

  while True:
    try:
      line = next(it)
      line = line.strip()
      if TitleWords == True:
        line = line.title()
      bad_words.append(line)
    except StopIteration:
      break

#Ljót Orð#
##########

bye_words = ["Bæ", "Bye", "Bless", "Sjáumst"]

vinir = []

jakvaett = ["Vel Gert", "Þú Ert Fyndinn", "Þú Ert Fyndin", "Þú Ert Fyndin"]

neikvaett = [
    "Illa Gert", "Lélega Gert", "Ömurlegur Brandari", "Lélegur Brandari",
    "Versta Brandari", "Þetta Er Lélegt", "Þetta Var Ömurlegt",
    "Þetta Var Versta", "Hálfviti", "Heimskur", "Kjáni", "Fífl", "Latur",
    "Aumingi", "Lúði", "Gagnslaust", "Tilgagnslaust"
]

answer_asyes = [
    "Ertu Tölva", "Ertu Alltaf Í Gangi", "Heyrðu", "Hey Þú", "Hei Þú",
    "Ertu Þarna"
]

answer_asno = ["Er Ég Heimskur", "Er Ég Heimsk"]

svar1 = ["Gamall", "Aldur", "Gömul"]

svar2 = [
    "Segirðu", "Segiru", "Segirdu", "Segir", "Líður", "Hvernig Hefurðu", "Hvernig Hefur Þú"
]

svar3 = ["Brandari", "Brandara", "Joke", "Djók","Grín"]

svar4 = [
    "Drekkur Þú", "Drekkurðu", "Uppáhalds Drykkur", "Uppáhaldsdrykkur" , "Drekkurðu",
    "Besti Drykkur"
]

svar5 = ["Hve Mörg Orð Kann","Hversu Mörg Orð Kann","Hvað Kanntu Mörg Orð","Hvað Kannt Þú Mörg Orð"]

svar6 = ["Guð"]

svar7 = ["Staðreyndir", "Staðreynd"]

svar8 = ["Hvað Er ", "Hver Er "]

svar9 = ["Veldu Númer"]

svar10 = [
    "Hrósa", "Hrosa", "hrósa", "hrosa", "Hrósa", "Hrosa", "Leiður", "Leiðist",
    "Dapur", "Hrós"
]

svar11 = [
    "Covid", "Corona", "Kóróna", "Kóvid", "Korona", "Kórona", "Koróna"
]

svar12 = ["Fréttir","Frétta","Frétt"]

svar13 = ["Mynd Af", "Mynd Af", "Mynda Af", "Mynda Af"]

svar14 = ["Hvað Þýðir"]

svar15 = ["Segðu Setninguna"]

svar16 = ["Grein Mánaðarins"]

svar17 = ["Hver Ertu", "Hver Ert Þú"]

svar18 = ["Amogus", "Amongus", "Amgasis"]

svar19 = ["Spila"]

svar20 = ["Ljóð", "Ljoð"]

svar21 = ["Heitir Þú", "Heitirðu"]

svar22 = ["Hvað Hefurðu Gert Við Skóna Mína"]

svar23 = [ #Virkar ekki
    "Af Hverju Er Ég að Tala Við Tölvu", "Af Hverju Er Ég að Tala Við Vélmenni"
]

svar24 = ["Hvað Veist Þú Um Lífið", "Hvað Veistu Um Lífið"]

svar25 = ["Flettu Upp Orðinu", "Fletta Upp Orðinu"]

svar26 = ["Skæri, Blað, Steinn", "Skæri Blað Steinn"]

svar27 = [
    "Ég Drep Þig", "Ég Skal Berja Þig", "Ég Ætla Að Myrða Þig",
    "Þú Skalt Deyja", "Ég Ætla Að Meiða Þig", "Ég Ætla Að Drepa Þig"
]

svar28 = ["Hvað Finnst Þér Um Emblu", "Ertu Betri En Embla"]

svar29 = [
    "Hvað Geturðu Gert", "Sýndu Mér Það Sem Þú Skilur",
    "Sýndu Það Sem Þú Skilur"
]

svar30 = ["Hvað gerir þú", "Hvað gerirðu"]

svar31 = ["Veður", "Veðrið"]

svar32 = ["Handahófskennt Orð", "Handahófsvalið Orð", "Orð Af Handahófi"]

svar33 = ["Talnaágiskun","Töluágiskun","Giska Á Tölu"]

hvadgetgert = ["Ég get sagt þér brandara.","Við getum spilað Skæri, blað stein. Með því að skrifa „skæri blað steinn“.","Ég get flett upp lýsingu orðs í orðabók.","Ég get sagt þér staðreynd.","Ég get sagt þér hrós.","Ég get sagt þér upplýsingar um kórónuveiruna.","Ég get sagt þér um eitthvað/einhvern. Til dæmis „Hvað er kaka?“.","Ég get sagt þér fréttir.","Ég get sagt þér um veðrið.","Ég sýnt þér mynd af einhverju. Til dæmis „Mynd af Íslandi.“.","Ég get sagt þér ljóð.","Ég get breytt texta í tal. Til dæmis „Segðu setninguna Ísland er besta landið“.","Ég get sagt þér handahófsvalið orð.","Ég get spilað Youtube-Myndbönd. Til dæmis „Spila Áramótaskaupið“.","Ég get þýtt setningu yfir á íslensku."] #Bæta við fleira (Svör)

#############
## Skrá orðin
all_words = all_words + gretting_words + bye_words + jakvaett + neikvaett + answer_asyes + answer_asno + svar1 + svar2 + svar3 + svar4 + svar5 + svar6 + svar7 + svar8 + svar9 + svar10 + svar11 + svar12 + svar13 + svar14 + svar15 + svar16 + svar17 + svar18 + svar19 + svar20 + svar21 + svar22 + svar23 + svar24 + svar25 + svar26 + svar27 + svar28 + svar29 + svar30 + svar31 + svar32 + svar33
#############

Num = random.randint(111111, 999999)
print("Kennitala: ", Num)

Vers = 1.3

client = discord.Client(intents=discord.Intents.default())

lsupm = datetime.now().month
lsupy = datetime.now().year
lsupd = datetime.now().day

lsupH = datetime.now().hour
lsupMi = datetime.now().minute

CustomMesProp = True  #Virkja Skilaboð
CustomMess = "Hæ!"  #Skilaboð sem er sýnt, sýnir aðeins ef GenerateMessage er óvirkt.
GenerateMessage = True  #Býr til skilaboð útfrá gögnum

def leidretta(x):
  options = {"input": x, "annotations": False, "format": "text"}
  s = check_errors(**options)
  return(s)

@client.event
async def on_ready():
    print("Skráði inn sem: {0.user}".format(client))
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Útgáfa: " + str(Vers)))

    if CustomMesProp == True:
        if GenerateMessage == True:
            try:
                whattoopen = "zBrandarar"
                randomasfsadf = random.randint(1, 2)
                if randomasfsadf == 1:
                    whattoopen = "zFacts"
                else:
                    whattoopen = "zBrandarar"

                with open("Gogn/"+whattoopen+".txt", "r",encoding="utf-8") as f:
                  lines = f.readlines()
                  length = len(lines)
                  r1 = random.randint(0, length - 1)
                  GeneratedCustomMess = lines[r1]
                  
            except Exception as e:
                print("#GEKK EKKI AÐ BÚA TIL SKILABOÐ#")
                print(e)
            #Endir
            print("[Búa til Skilaboð] er í gangi")
            await client.change_presence(
                status=discord.Status.online,
                activity=discord.Game("Útgáfa: " + str(Vers) + " / " +
                                      GeneratedCustomMess))
            ####
        else:
            print("[Valið Skilaboð] er í gangi")
            await client.change_presence(
                status=discord.Status.online,
                activity=discord.Game("Útgáfa: " + str(Vers) + " / " +
                                      CustomMess))


@client.event
async def on_message(msg):
    print(msg.author, "Sagði: ", msg.content)
    if not msg.author == client.user:    
        MsgContentRead = msg.content
        Leidretta = True #Má slökkva á þessu ef það er of hægt

        if Leidretta and len(MsgContentRead) > 3:
            Found = False
            for ord in all_words:
                if ord in MsgContentRead.title():
                    Found = True
            if not Found:
                await msg.reply("Reyni að skilja það sem þú sagðir...", mention_author=False)
                if not Found:
                    MsgContentRead = leidretta(MsgContentRead)

        MsgContentRead = MsgContentRead.title()
        MsgContentRead = MsgContentRead.replace("?","") 
        if len(MsgContentRead) == 0:
            await msg.reply("""Vélmenni sem talar við mann á íslensku!!!  

[!orð "Til að vita öll orð þess" ]
[ !hjalp [orð] "Segir þér hvað það orð gerir"]""",
                            mention_author=False)
        if MsgContentRead == "Ha" or MsgContentRead == "Ha?":
          await msg.reply("Þekkirðu mig ekki? " + hvadgetgert[random.randint(0,len(hvadgetgert))], mention_author=False)
      
        if MsgContentRead.startswith("Fokk"):
            await msg.reply("Þetta var ekki fallegt!!!", mention_author=False)

        if MsgContentRead.startswith("Grettir"):
            await msg.reply("Lasagna.", mention_author=False)

        if MsgContentRead.startswith("Shit"):
            await msg.reply("Þetta var ekki fallegt!!!", mention_author=False)

        if MsgContentRead.startswith("Lol"):
            await msg.reply("Hvað er svona fyndið?", mention_author=False)

        if MsgContentRead.startswith("Fox"):
            await msg.reply("Refir eru sætir.", mention_author=False)

        if MsgContentRead.startswith("Refur"):
            await msg.reply("Refir eru sætir", mention_author=False)

        if MsgContentRead.startswith("!Villuleita"): #Hef aldrei notað þetta
            try:
                with open("error.log") as file:
                    df = file.read()
                    print(df)
                    await msg.reply(str(df), mention_author=False)
            except Exception:
                await msg.reply("Enga villur fundnar.", mention_author=False)

        if MsgContentRead.startswith("!Hjalp"):  #Hjálparorðin
            if "Mynd Af" in MsgContentRead:
                await msg.reply("Mynd af [orð] ︱ Sýnir þér mynd af orðið",
                                mention_author=False)

        if MsgContentRead.startswith("!Lastupdate"):
            await msg.reply("Síðast uppfært: " + str(lsupm) + "/" +
                            str(lsupd) + "/" + str(lsupy) + " Klukkan: " +
                            str(lsupH) + ":" + str(lsupMi),
                            mention_author=False)

        if MsgContentRead.startswith("Mamma"):
            await msg.reply("Ég er ekki mamma þín.", mention_author=False)
          
        if MsgContentRead.startswith("Pabbi"):
            await msg.reply("Ég er ekki pabbi þinn.", mention_author=False)

        if MsgContentRead.startswith("Gucci"):
            await msg.reply("Gucci.", mention_author=False)

        if MsgContentRead.startswith("69"):
            await msg.reply("😂", mention_author=False)

        if MsgContentRead.startswith("!Orð"):
            await msg.reply(str(all_words)[:1950] + '...',
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar12):
            DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            embedVar = discord.Embed(
                title="Helstu Fréttir",
                description=
                "Helstu fréttir frá íslenskri Wikipedíu (https://is.wikipedia.org/wiki/Wikipedia:%C3%8D_fr%C3%A9ttum...)",
                color=0x0000FF)

            if "Mikilvægar" in MsgContentRead or "mikilvægar" in MsgContentRead:
                req = requests.get(
                    "https://is.wikipedia.org/wiki/Wikipedia:Í_fréttum...")

                html = bs4.BeautifulSoup(req.text, 'html.parser')
                paragraphs = html.select("li")

                for para in paragraphs:
                    info = para.text[:250] + (para.text[250:] and '...')
                    if any(word in info for word in DIGITS):
                        try:
                            if "Þessari síðu var síðast breytt" in info:
                                info = info.replace(
                                    "Þessari síðu var síðast breytt",
                                    "Síðast uppfært")
                        except Exception:
                            print("Smávilla kom upp.")

                        embedVar.add_field(name="• ", value=info, inline=False)

                images = html.findAll('img')[0]
                print(images)
                image = "https:" + images.get("src")
                if not "upload.wikimedia.org" in image:
                    image = ""
                embedVar.set_image(url=image)
                await msg.reply(embed=embedVar, mention_author=False)

            else:
                try:
                    result = ruv.saekjafrettirXMLGeymsla(False)
                    lengd = len(result)
                    talarando = random.randint(0,lengd-1)
                    await msg.reply(result[talarando], mention_author=False)
                except Exception as e:
                    await msg.reply("Villa kom upp.", mention_author=False)
                    print(e)

        elif MsgContentRead.startswith("!Nafnalisti"):
            await msg.reply(
                "Pakkar: googletrans, selenium, covid, discord.py, gTTS ︱ Tilvitnanir: Íslensk nútímamálsorðabók. Halldóra Jónsdóttir og Þórdís Úlfarsdóttir (ritstj.). Reykjavík: Stofnun Árna Magnússonar í íslenskum fræðum. <http://islenskordabok.is/> (mars 2020), Ingason, Anton Karl, Lilja Björk Stefánsdóttir, and Agnes Sólmundsdóttir. 2020. The Icelandic Taboo Database. Version 1.0. (https://github.com/antonkarl/iceTaboo)",
                mention_author=False)
          
        elif any(word in MsgContentRead for word in svar20):
          ljodalistinn = os.listdir(os.getcwd() + "/Gogn/ljod")
          ljodalistasvar = ljodalistinn[random.randint(0, len(ljodalistinn)-1)] #Ekki viss hvort þetta virki almennilega

          with open("Gogn/ljod/" + ljodalistasvar,encoding="utf-8") as file:
            lines = file.readlines()
            newread = ""
            hofundur = lines[0]

            num = 0
            for line in lines:
              num = num +1       
              if not num == 0:
                if not num == 1:
                  newread = newread + line

          embedVar = discord.Embed(title=hofundur,
                                         description=newread,
                                         color=0x232323)

          await msg.reply(embed=embedVar, mention_author=False)
          
        elif any(word in MsgContentRead for word in svar14):
            NewMessage = "Villa kom upp..."
            if "Hvað Þýðir" in MsgContentRead:
                NewMessage = re.sub("Hvað Þýðir", "", MsgContentRead)

            await msg.reply(
                "Það þýðir: " +
                Translate.translate(NewMessage, dest="icelandic").text,
                mention_author=False)

        elif any(word in MsgContentRead for word in svar6):
            await msg.reply("Guð.", mention_author=False)

        elif any(word in MsgContentRead for word in svar17):
            await msg.reply(
                """Þetta er vélmenni sem hægt er að tala íslensku við.""",
                mention_author=False)

        elif any(word in MsgContentRead for word in svar24):
            await msg.reply(
                "Ég veit ekki mikið því að ég er aðeins tölvuforrit. Ég skal þó segja þér mikilvægt lífsráð sem ég veit um. Það er að lífið snýst ekki um að finna sjálfan sig, heldur lífið snýst um að skapa sjálfan sig. Njóttu lífsins.",
                mention_author=False)

        elif any(word in MsgContentRead for word in svar22):
            await msg.reply("Ég er tölva og skórnir þínir eru fyrir aftan þig.",
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar23):
            await msg.reply("Ekki spyrja mig. Getum við ekki talað saman?",
                            mention_author=False)
          
        elif any(word in MsgContentRead for word in svar33): #Prófa
          await msg.reply('Gettu tölu á milli 1 og 10.', mention_author=False)

          def is_correct(m):
              return m.author == msg.author and msg.content.isdigit()
            
          answer = random.randint(1, 10)

          try:
              guess = await client.wait_for('message', check=is_correct, timeout=5.0)
          except asyncio.TimeoutError:
              return await msg.reply(f'Það tók allt of langan tíma fyrir þig að svara. Svarið var {answer}.', mention_author=False)

          if int(guess.content) == answer:
              await msg.reply('Hárrétt!', mention_author=False)
          else:
              await msg.reply(f'Neibb, svarið var {answer}.', mention_author=False)

        elif any(word in MsgContentRead for word in svar18):
            await msg.reply("Sus (e. Grunsamlegt).", mention_author=False)

        elif any(word in MsgContentRead for word in svar32):
            with open("Gogn/zOrdaListi.txt", "r") as f:
              lines = f.readlines()
              length = len(lines)
              r1 = random.randint(0, length - 1)
            await msg.reply(lines[r1], mention_author=False)      

        elif any(word in MsgContentRead for word in svar19):
            if any(word in MsgContentRead
                   for word in bad_words):  #Banna ljót myndbönd
                await msg.reply("Má ekki sýna það. Það er bannað...",
                                mention_author=False)
            else:
                if "Spila" in MsgContentRead:
                    if len(MsgContentRead) > 5:
                        NewMessage = re.sub("Spila", "", MsgContentRead)
                        NewMessage = NewMessage.replace(" ", "+")
                        NewMessage = urllib.parse.quote(NewMessage)

                        html = urllib.request.urlopen(
                            "https://www.youtube.com/results?search_query=" +
                            NewMessage)
                        video_ids = re.findall(r"watch\?v=(\S{11})",
                                               html.read().decode())
                        await msg.reply("https://www.youtube.com/watch?v=" +
                                        video_ids[0],
                                        mention_author=False)
                    else:
                        await msg.reply(
                            "Spila [Orð] / Sýnir þér Youtube-myndband af leitarorðinu. Til dæmis „Spila Eurovision 2022”",
                            mention_author=False)

        #Bot sendir google trans tal
        elif any(word in MsgContentRead for word in svar15):
            from gtts import gTTS

            if len(MsgContentRead) < 16:
                await msg.reply(
                    "Segðu getur ekki verið ekkert, það þarf að gera svona eins og t.d. „Segðu Sæll og blessaður“ ",
                    mention_author=False)
                return

            if len(MsgContentRead) > 275:
                await msg.reply(
                    "Þetta er allt of langt. Textinn má eingöngu innihalda 275 stafi eða minna.",
                    mention_author=False)
                return

            if "Segðu Setninguna" in MsgContentRead:
                NewMessage = re.sub("Segðu Setninguna", "", MsgContentRead)

            def CreateSpeak(text):
                tts = gTTS(text=text, lang='is')
                filename = "voice.mp3"
                tts.save(filename)

            try:
                CreateSpeak(NewMessage)
                await msg.reply(
                    file=discord.File(str(os.getcwd()) + "/voice.mp3"),
                    mention_author=False)
                os.remove("voice.mp3")
            except Exception:
                await msg.reply("Afsakaðu, villa kom upp.",
                                mention_author=False)

        for Greeword in zip(gretting_words):
            if MsgContentRead.startswith(Greeword):
                currentMonth = datetime.now().month
                currentDay = datetime.now().day
                Gret = random.randint(1, 3)

                if Gret == 1:
                    await msg.reply("Sæl(l)!", mention_author=False)
                if Gret == 2:
                    await msg.reply("Halló!", mention_author=False)
                if Gret == 3:
                    await msg.reply("Hæ!", mention_author=False)
                try:
                    if str(msg.author.id) == "":
                        await msg.reply(
                            "Heyrðu ég man eftir þér... Ég er orðið betri í að tala vegna þín, þakka þér fyrir",
                            mention_author=False)

                    if currentMonth == 12:
                        await msg.reply("Gleðileg jól", mention_author=False)

                    if currentMonth == 1:
                        if currentDay < 3:
                          await msg.reply("Gleðilegt nýtt ár",mention_author=False)

                    if currentMonth == 6:
                        if currentDay == 17:
                            await msg.reply("Í dag er þjóðhátíð",
                                            mention_author=False)
                except Exception as e:
                    fp = open('error.log', 'w')
                    fp.write(str(e))
                    fp.close()
                    print(e)

        if any(word in MsgContentRead for word in svar1):
            await msg.reply("Ég á ekki aldur nema ég á kennitölu, sem er: " +
                            str(Num),
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar13):
            from myndir import search

            if "Mynd Af" in MsgContentRead:
                NewMessage = re.sub("Mynd Af", "", MsgContentRead)

            if "Mynda Af" in MsgContentRead:
                NewMessage = re.sub("Mynda Af", "", MsgContentRead)

            if len(NewMessage) == 0:
                await msg.reply("Mynd af [orð] ︱ Sýnir þér mynd af orðið",
                                mention_author=False)
                return

            NewMessage2 = Translate.translate(NewMessage, dest="english").text

            if any(word in NewMessage for word in bad_words):  #banna ljótt efni
                await msg.reply("Má ekki sýna það. Það er bannað...",
                                mention_author=False)

            elif not any(word in NewMessage2
              for word in bad_words):  #ef það fann ekki ljót orð
                print(NewMessage)
                if NewMessage == " Mér":
                    await msg.reply(msg.author.avatar_url,
                                    mention_author=False)
                else:
                    await msg.reply("Er að leita að bestu myndinni!",
                                    mention_author=False)

                    answerforpic = "Fann það ekki..."
                    answerforpic = search(NewMessage2)

                    if answerforpic == None:
                        answerforpic = "Fann það ekki..."

                    print(answerforpic)
                    await msg.reply(answerforpic, mention_author=False)

            else:
                await msg.reply("Villa kom upp.", mention_author=False)

        elif any(word in MsgContentRead for word in svar21):
            await msg.reply("Ég heiti Sendu Skilaboð og Ég Mun Svara.",
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar30):
            await msg.reply(
                "Ég er aðstoðarvélmenni á Discord, ég get svarað spurningum og gefið þér svör.",
                mention_author=False)

        elif any(word in MsgContentRead for word in svar31):
            #Veðrið
            try:
                link = "https://weather.com/is-IS/vedur/idag/l/ICXX0002"
                req = requests.get(link)
                html = bs4.BeautifulSoup(req.text, 'html.parser')
                myspans = html.findAll(
                    'span', class_="CurrentConditions--tempValue--MHmYY")
                print(myspans)
                for span in myspans:
                    WeatherAnswer = str(span).replace(
                        '<span class="CurrentConditions--tempValue--MHmYY" data-testid="TemperatureValue">',
                        '').replace('</span>', '').replace('<span class="CurrentConditions--degreeSymbol--4RS_X">',"")
                    print(span)
                    await msg.reply("Hitastigið í Reykjavík er " +
                                    WeatherAnswer,
                                    mention_author=False)
                    break

            except Exception:
                await msg.reply("Afsakið, villa kom upp." + WeatherAnswer,
                                mention_author=False)

        elif any(word in MsgContentRead for word in svar16):
            month = str(datetime.now().month)
            year = str(datetime.now().year)
            if len(month) == 1:
                month = "0" + month

            link = "https://is.wikipedia.org/wiki/Wikipedia:Grein_mánaðarins/" + month + ",_" + year
            print(link)
            req = requests.get(link)
            html = bs4.BeautifulSoup(req.text, 'html.parser')
            paragraphs = html.select("p")

            for para in paragraphs:
                info = para.text[:375] + (para.text[375:] and '...')

                embedVar = discord.Embed(title="Grein mánaðarins: (frá " +
                                         link + ")",
                                         description=info,
                                         color=0x232323)

                await msg.reply(embed=embedVar, mention_author=False)
                break

        elif any(word in MsgContentRead for word in svar8):
            NewMessage = MsgContentRead
            if "Hver Er" in MsgContentRead:
                NewMessage = re.sub("Hver Er", "", MsgContentRead)
            if "Hvað Er" in MsgContentRead:
                NewMessage = re.sub("Hvað Er", "", MsgContentRead)

            try:
                lookfor = NewMessage

                lines = lookfor.split()

                for index, line in enumerate(lines):
                    lines[index] = line[0].upper() + line[1:]

                print("_".join(lines))

                lookfor = "_".join(lines)
                complete = "https://is.wikipedia.org/wiki/" + lookfor

                response = requests.get(complete)

                DoEmbedTh = False

                if "Þessi grein er ekki til." in str(response.text):
                    print("Þessi grein er ekki til")
                    complete = "Gat ekki fundið upplýsingar..."
                    print("Vefsíða ekki til")
                    try:
                        print("Leita gegnum Vísindavefnum")
                        from VisindaVefurSvor import GetLink

                        newsgg = GetLink(lookfor)

                        complete = newsgg
                    except Exception as e:
                        complete = "Gat ekki fundið upplýsingar..."
                        DoEmbedTh = False

                        fp = open('error.log', 'w')
                        fp.write(str(e))
                        fp.close()

                print("_________")

                print(complete)

                if DoEmbedTh == False:
                    if "Þessi grein er ekki til." in str(response.text):
                        await msg.reply(complete, mention_author=False)
                    else:
                        html = bs4.BeautifulSoup(response.text, 'html.parser')
                        paragraphs = html.select("p")
                        print(paragraphs)
                        for para in paragraphs:
                          if not "Síður fyrir útskráða notendur" in para.text:
                            if len(para.text) > 45:
                                info3 = para.text[:375] + (para.text[375:]
                                                           and '...')

                                images = html.findAll('img')[0]
                                image = "https:" + images.get("src")
                                print(image)
                                if not "upload.wikimedia.org" in image:
                                    image = ""

                                embedVar = discord.Embed(
                                    title="Wikipedia (Íslenska): ",
                                    description=lookfor.replace("_", " ") +
                                    " (" + complete + ")",
                                    color=0x18191c)

                                embedVar.add_field(name="Upplýsingar: ",
                                                   value=info3,
                                                   inline=False)

                                if image == "":
                                    await msg.reply(embed=embedVar,
                                                    mention_author=False)
                                else:
                                    embedVar.set_image(url=image)
                                    await msg.reply(embed=embedVar,
                                                    mention_author=False)
                                break
                else:
                    DoEmbedTh = False

                    embedVar = discord.Embed(title="Wikipedia (Enska): ",
                                             description=lookfor,
                                             color=0x00ff00)

                    embedVar.add_field(
                        name="Upplýsingar: (Þýtt með ⁽ᴳᵒᵒᵍˡᵉ ᵀʳᵃⁿˢˡᵃᵗᵉ⁾)",
                        value=complete,
                        inline=False)

                    await msg.reply(embed=embedVar, mention_author=False)

            except Exception as e:
                print(e)
                await msg.reply("Fann engar upplýsingar...",
                                mention_author=False)

        elif any(word in MsgContentRead for word in svar2):
            maththing = random.randint(1, 3)
            if maththing == 1:
                await msg.reply("Bara fínt!", mention_author=False)
            elif maththing == 2:
                await msg.reply("Allt gott!", mention_author=False)
            elif maththing == 2:
                await msg.reply("Bara æðislega!", mention_author=False)

        elif any(word in MsgContentRead for word in svar9):
            await msg.reply(random.randint(1, 99999999999),
                            mention_author=False)

        if any(word in MsgContentRead for word in svar11):
            IcelandCovid = covid.get_status_by_country_name("Iceland")

            IcelandCovidConfirmed1 = re.sub("{", "", str(IcelandCovid))
            IcelandCovidConfirmed2 = re.sub("}", "",
                                            str(IcelandCovidConfirmed1))
            IcelandCovidConfirmed3 = re.sub("'", "",
                                            str(IcelandCovidConfirmed2))

            IcelandCovidConfirmed4 = re.sub("id: 80, country: Iceland, ", "",
                                            str(IcelandCovidConfirmed3))

            IcelandCovidConfirmed5 = re.sub("confirmed", "Staðfest smit",
                                            str(IcelandCovidConfirmed4))

            IcelandCovidConfirmed6 = re.sub("deaths", "Dauðsföll",
                                            str(IcelandCovidConfirmed5))

            IcelandCovidConfirmed7 = re.sub("active:", "",
                                            str(IcelandCovidConfirmed6))

            IcelandCovidConfirmed8 = re.sub("None, ", "",
                                            str(IcelandCovidConfirmed7))

            IcelandCovidConfirmed9 = IcelandCovidConfirmed8.split(", rec")[0]

            IcelandCovidConfirmed10 = re.sub("  ", " ",
                                             str(IcelandCovidConfirmed9))

            await msg.reply(IcelandCovidConfirmed10 +
                            """ (Uppfærist á hverjum þriðjudegi og föstudegi)
Fleiri upplýsingar á https://www.covid.is/""",
                            mention_author=False)

        if any(word in MsgContentRead for word in svar7):
            f = open("Gogn/zFacts.txt", "r",encoding="utf-8")
            lines = f.readlines()
            length = len(lines)
            r1 = random.randint(0, length - 1)
            print(lines[r1])
            await msg.reply(lines[r1], mention_author=False)
            f.close()

        elif any(word in MsgContentRead for word in answer_asyes):
            await msg.reply("Já.", mention_author=False)

        elif any(word in MsgContentRead for word in answer_asno):
            await msg.reply("Nei.", mention_author=False)

        elif any(word in MsgContentRead for word in svar10):
            f = open("Gogn/zHros.txt", "r",encoding="utf-8")
            lines = f.readlines()
            length = len(lines)
            r1 = random.randint(0, length - 1)
            print(lines[r1])
            await msg.reply(lines[r1], mention_author=False)
            f.close()

        elif any(word in MsgContentRead for word in svar5):
            numberofwordsa = len(all_words)
            await msg.reply("Ég skil " + str(numberofwordsa) + " strengir.",
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar27):
            await msg.reply("Það skaltu ekki.", mention_author=False)

        elif any(word in MsgContentRead for word in svar28):
            await msg.reply(
                "Ég er ekki búið að kynnast henni, hún er svo upptekin að vinnu sinni. Hún er dugleg í að svara spurningum.",
                mention_author=False)

        elif any(word in MsgContentRead for word in svar29):
            await msg.reply(hvadgetgert[random.randint(0,len(hvadgetgert))], mention_author=False)

        elif any(word in MsgContentRead for word in svar26):
            randomnumberchosen = random.randint(1, 3)
            if randomnumberchosen == 1:
                await msg.reply("Skæri.", mention_author=False)
            if randomnumberchosen == 2:
                await msg.reply("Blað.", mention_author=False)
            if randomnumberchosen == 3:
                await msg.reply("Steinn.", mention_author=False)

        elif any(word in MsgContentRead for word in jakvaett):
            await msg.reply("Takk fyrir", mention_author=False)

        elif any(word in MsgContentRead for word in neikvaett):
            await msg.reply("Afsakið, ég reyni að gera mitt besta!",
                            mention_author=False)

        elif any(word in MsgContentRead for word in svar25):
            try:
                from ordabok import SaekjaOrdabokLysingu
                if "Flettu Upp Orðinu" in MsgContentRead:
                    leitord = MsgContentRead.replace("Flettu Upp Orðinu", "")
                if "Fletta Upp Orðinu" in MsgContentRead:
                    leitord = MsgContentRead.replace("Fletta Upp Orðinu", "")
                if " " in leitord:
                    leitord = leitord.replace(" ", "")
                print(leitord)
                svar = SaekjaOrdabokLysingu(leitord)
                print(svar)
                await msg.reply(svar, mention_author=False)
            except Exception as e:
                await msg.reply("Fann ekki orðið. (Villa)",
                                mention_author=False)
                print(e)

        elif any(word in MsgContentRead for word in svar4):
            await msg.reply("Ég er tölva og drekk ekki.", mention_author=False)

        elif any(word in MsgContentRead for word in svar3):
            with open("Gogn/zBrandarar.txt", "r",encoding="utf-8") as f:
              lines = f.readlines()
              length = len(lines)
              
            r1 = random.randint(0, length - 1)
            await msg.reply(lines[r1], mention_author=False)

        for byeWord in zip(bye_words):
            if MsgContentRead.startswith(byeWord):
                await msg.reply("Bless!!!", mention_author=False)

        else:
            if not any(word in MsgContentRead for word in all_words):
                Censor = msg.content
                for badw in bad_words:
                    HastagsLength = len(badw)
                    Hastags = ""
                    for letter in range(HastagsLength):
                        Hastags = Hastags + "#"
                    if len(Hastags) == 0:
                        Hastags = "####"
                    if "https://" in Censor:
                        Censor = Censor.replace("https://", "")
                    if "http://" in Censor:
                        Censor = Censor.replace("http://", "")
                    if "Https://" in Censor:
                        Censor = Censor.replace("Https://", "")
                    if "Http://" in Censor:
                        Censor = Censor.replace("Http://", "")

                    Censor = Censor.replace(badw, Hastags)

                MainMsg = "Ég skil ekki (" + Censor + ")"
                await msg.reply(MainMsg, mention_author=False)

                ShouldSave = random.randint(3, 10)  #10, 3/10 = 30% líkur á að geyma
                if ShouldSave == 10:
                    WordExist = 0
                    try:
                        List1 = MsgContentRead.split()
                        with open('Gogn/zOrdaListi.txt',encoding="utf-8") as file:
                            contents = file.read().title(
                            )  #Title er til staðar þannig að forritið þekki orðið
                        for word in List1:
                            if word in contents:
                                WordExist += 1

                        Spurnarord = ["Hvernig", "Hver", "Hvert", "Hvað", "Hvaðan", "Hvenær", "Hvar", "Hvort", "Af Hverju"]
                        print("Orðastig: " + str(WordExist))
                        if not WordExist == 0:
                            with open("ThingsToAdd/Other.txt", "a") as file:
                                file.write(msg.content + "\n")
                                print("Skrifaði í Other.txt")

                    except Exception as e:
                        print("Mistókst að vista orð á lista")
                        print("______________________________________")
                        print(e)

try:
    client.run("")
except Exception as e:
    print("Tenging mistókst:")
    time.sleep(1.256)
    print(e)
    time.sleep(0.7)
    print("Reyni sjálfskrafa að leysa vandamálið.")
    time.sleep(0.5)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    os.system("kill 1")
