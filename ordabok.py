import requests
import json
def SaekjaOrdabokLysingu(ordid):
  if " " in ordid:
    ordid = ordid.replace(" ","")

  ReturnWord = "Fann ekki orðið."

  ordid = ordid.lower()#
  req1 = requests.get("https://islenskordabok.arnastofnun.is/django/api/es/flettur/?fletta={a}*&simple=true".format(a = ordid))
  y = json.loads(req1.text)

  #Reyndi að herma eftir þessu og nennti aldrei að laga það: https://github.com/mideind/Greynir/blob/4e4398a6067fbbf6c9dd0786b0c1224663e1841d/queries/dictionary.py

  for i in range(len(y["results"])):
    if y["results"][i]["fletta"] == ordid: #.title()
      kodinn = y["results"][i]["flid"]
      req2 = requests.get("https://islenskordabok.arnastofnun.is/django/api/es/fletta/{a}/?lang=IS".format(a = kodinn)) #hús er 
      k = json.loads(req2.text)
      print(k)
      print("________________")
      ss = False
      try:
        blandasamanlistann = []
        for i in range(len(k["items"])):
          print(k["items"][i]["teg"])
          if k["items"][i]["teg"] == "LIÐUR":
            try:
              numbertogotoo = k["items"][i]["num"]
              if k["items"][numbertogotoo]["teg"] == "SKÝRING":
                print("Liður")
                print(k["items"][numbertogotoo]["texti"])
                blandasamanlistann.append(k["items"][numbertogotoo]["texti"])
                ReturnWord = "1."+blandasamanlistann[0] + "2." + blandasamanlistann[1]
                return ReturnWord
                break
            except Exception:
              if k["items"][i]["teg"] == "SKÝRING":
                print("Ekki Liður")
                print(k["items"][i]["texti"]) #13 fyrir hús
                print(k["items"][len(k["items"])-3]["texti"]) #13 fyrir hús
                break
          else:
            if ss == False:
              if k["items"][i]["teg"] == "SKÝRING":
                print("Ekki Liður")
                svarid = k["items"][i]["texti"]
                print(k["items"][i]["texti"]) #13 fyrir hús
                ReturnWord = svarid
                
                print(k["items"][len(k["items"])-3]["texti"]) #13 fyrir hús
                return ReturnWord
                break
      except Exception:
        print("Villa kom upp")
