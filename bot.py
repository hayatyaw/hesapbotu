import requests
import sys
import os
import random
import colorama
import pyautogui
import time
import string
import pytesseract
from discord_webhook import DiscordWebhook
import getpass, os, uuid, hashlib, getmac as gma
import psutil
import subprocess

def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

if check_if_process_running("fiddler.exe") == True:
    DiscordWebhook(url="https://discord.com/api/webhooks/1192890910002905240/Iunia8s55bk_vN93Q9QuWh0EUGciLolJGwRaG4bjgiKbnuZNQ5SJrgMhpO83sosIxz2y", content=f"FIDDLER DETECTED\nHWID: {(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}").execute()
    quit()
if check_if_process_running("httpdebugger.exe") == True:
    DiscordWebhook(url="https://discord.com/api/webhooks/1192890910002905240/Iunia8s55bk_vN93Q9QuWh0EUGciLolJGwRaG4bjgiKbnuZNQ5SJrgMhpO83sosIxz2y", content=f"HTTP DEBUGGER DETECTED = {{(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}}").execute()
    quit()

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def temizlik():
    os.system("cls")
    time.sleep(0.2)

def hwidAl():
        hwidAlmak = hashlib.sha384((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest()
        return hwidAlmak

webhooklink = "https://discord.com/api/webhooks/1192890910002905240/Iunia8s55bk_vN93Q9QuWh0EUGciLolJGwRaG4bjgiKbnuZNQ5SJrgMhpO83sosIxz2y"

strin = ['RZvXOtVKGgYLLHkuzcuErNKjYlBBhV.txt', 'YAPgtiEpbjCSSlPKswqesfypQORMcW.txt', 'TonHiQCoxHCUoHVAYabCRMpRSGtWwr.txt', 'UnVEJbkzEhatoCjSwCgVsoSLGPmaGX.txt', 'NNUNnDLvfSJcboGcaIYxgYRgqVaRBY.txt', 'EDQRbAQRZqHOqcCpclHiXKnGElwxBe.txt', 'lviQegsIpziVjluRBkaXBZRZddKDxk.txt', 'KtEDDVbGELAvyGeWSqYYUXPIOLeLEh.txt', 'ryMsGLgaYLjeJXtjMztMpTFjxcIqec.txt', 'sAegqnfNUttAaxbIqCGlfkZZQLGSAN.txt', 'gwJWJcOPRKFNxYbmrPLMBPoaFILoBh.txt', 'qdlDApQtxFBbkLxJDUQKWeWaaESvlf.txt', 'xDGjXTYhYoyYlObUmGhhUZOOMwXjmi.txt', 'iMFHnJDCNWVcsbnWiEyIZCqsySupuP.txt', 'ihsIIIZfTePIhhQPdAtoleBniLcUFv.txt', 'OQeweMrmAKFTtyPYTwzWuQKVmdBxhz.txt', 'BfUNqvbVPKnuaDWaCQHnHEaJQoSLkY.txt', 'ymLJcGmtxOoMNAjFjwPUFHkrVTcNpG.txt', 'bXwilZonerVUtnsKRKnEduvYDauOOa.txt', 'jNtZhQfZlHhqQGSxXfrFUTpWZmtbRo.txt', 'aJUovIBPsXuxMocwAPCqedANKVKzsO.txt', 'dpvMjWASaBbNnzoRiYgLKRzlNkcPzS.txt', 'ckpejKPAbNhRrNGfugxOiQMtFiWxEv.txt', 'WmdTnfQiUEzszDdcbUkMGKAnkkOvjS.txt', 'SrCUhlvjTpOzvnENjKpykZQVDrCJPM.txt', 'nfkOAoTAQbxJcNRcsdjmuvjlJgtUSm.txt', 'xVfNYndKnWqwyxBnHYOsCIzMMHPsbW.txt', 'oEvIVihbdjAFjhcYxVjVlACupzNyQY.txt', 'baaZKBAVmAdPmajvQeNMesMmGMeocR.txt', 'MLqYsmydNFGRbGIuiwoCdbRgDeDOdK.txt', 'EIKDnbKlvXXEuecZktzmyagJMGFkLs.txt', 'UEyjxBHpSmzFodnETZLDOYxsAjLFKe.txt', 'PJxRDAswxCbKvFIiBcNWDhJtIGXrkC.txt', 'aPFrnArBivFhzdUHAkuRWBjkQoUYmw.txt', 'BApiMSLkvtWDoACnbvgrzrNyQFBHke.txt', 'gPbkomLwzbKbjlCOVfnuETUdjetCWh.txt', 'HPDtAKSfxpkCECHbxKspvOWHDykRXr.txt', 'dsAuwcuVQWLtgyUNtlTOWLdbxYKxdo.txt', 'yHtPOJZWGgAZZocdQCkgnFJHlvsEAy.txt', 'tYXlepBCoiIHrFkfrVqFcZVvrTseIG.txt', 'xPuDUCnsHsXNPYHkWRxjKVhvAoLRmQ.txt', 'BJpEYsGZiNBsyqFjOrVtsJNkjaMGBf.txt', 'OmCWxatjCDCTgRCsmUSKbawdieStfT.txt', 'EcbWfHBYbyyOAgibPCBJonsafSBqUH.txt', 'jnrVdkCMWfsawBpiRwGxbqHbgUXdeH.txt', 'HfObatYCsblqfFESzWfFGEstTRgqkw.txt', 'CgQnhwJQTxNRwOtWWJlGDtlDWNpjyf.txt', 'KrOfgvBZzwaFdWbpmApHlAfmoBqLPr.txt', 'pqcPXWDEJJomhLYLrUytZKhlHvlGaC.txt', 'LGEQGeJMKWVxYKcxEvuRfVoUQPOEbu.txt', 'flFWIhkBornLWcEMbUeBWIbuamFlhb.txt', 'dgGsheLfKsLbDMBYSQoAZbxEgYmmzH.txt', 'QUsnWBTxTgTMitzepwHNxReNBgRESA.txt', 'nOHmeJGQWbmHCUIHOViMwKLCRCNVRF.txt', 'QBhUnvpBjRyzAfwDnPOfiyWQMEXivN.txt', 'gjgxvvomoxmQSjUZtpBIKYdidAUnMh.txt', 'sCBkMHdRQnHbxHWNWgyvNcRHNJeTUE.txt', 'ZSzZhRZmYMCFFLJhRRhvNPrmPQBtnt.txt', 'fSaYGJwASWWDHKhZyfMaOhpaVqJlqd.txt', 'BsnHpXSXcntqRicbUcQoQXMDFfwdTk.txt', 'YxgZqHAykYtjnPJoRfxjEGnlwKijxx.txt', 'OCiMFFqZsHJHPXpFKTFTFKmVgzHqcI.txt', 'tRzaPgJxbvjYjcZZBcqGOKOKbiNuot.txt', 'cmLClpbnmVfoaYARcxrRvKhpnKJsdw.txt', 'WoPxIyxpnjMYReVGZAqKJvDGnMnaWi.txt', 'sexGIKZLyQvLfJwmqrjGQhtYzazJdK.txt', 'MtAnaguLkgTFfMLXDSggdRJfkOKEpv.txt', 'gKzwhdekYZPWTMdfSGKnVqvmobmJSB.txt', 'enNkXXYCkRqfdTcNkeOoAmTflJLXHj.txt', 'bRHgFYPfuAbngmjhHFFiXVQKafGHmz.txt', 'rWpcQfMBHWdAMEJHvTvaxSkEfdMwPg.txt', 'FcvtXCEQIrJihZrxzaLmScnUZwUpoA.txt', 'CcBxdCzmfuLiNOZAiePCokeRSRKhGB.txt', 'cUuvHTqKIvOaNgCrEMsOlIySzzWhhJ.txt', 'NkrNFCORETtglZtbWyjuMHgPvGuyVn.txt', 'LbmMoKDnlbgZQmvyhlqMaTfmhZIEjr.txt', 'tSSddcRoRSlqwobCpJXQQVDimMsxSm.txt', 'dcsdXZqqBbiJkjRQYaxmWffCKNshby.txt', 'dgDuHlIsHmJTPbOofiypJYtWxGWJgp.txt', 'XUQAlZgLMVeXNbDFvkqiFZftkcWQuj.txt', 'tFazyMeHmlOePOgIEdvWpuSBQxVwar.txt', 'sTkPCtAnghhqHSszRfNGhXKiPifsCY.txt', 'sblobuhOlDxMgnFPrgAjaDYWVqoZCX.txt', 'SDsLixPvMloLjfVZKQKiKAMGJtTwXv.txt', 'hZowAPQtvbktADhOUZNUGOKlgLRqJh.txt', 'BWnBQwzewIlGPLqsVWenCbhSobkSQM.txt', 'cAQakLYDvsUhssPdmTtnoDBwtDFzpk.txt', 'GzVODVhqCbDSNxyTrfmZNzlGTpXPNJ.txt', 'xgwZPRHPjYNjkhAqYAFpAAJsvprjFA.txt', 'qgKFxcILVUxTlqAwcdUJYzihAVBKRm.txt', 'lMKsjGESVxAuNqWUceuMiWNbhBRynm.txt', 'iQgsyYysWAMTdiICphblRsyfAmhMbF.txt', 'rNAwpdMXhjfCMBFowUuBCEXOAwinTu.txt', 'hUMWVUCFNAnEewreMHHYHcKxCGfYCb.txt', 'ecmFWaxtgIOrVQqWEIajqMkNbvfMwH.txt', 'rwaTAvzKIxxKXYDGsgeKgJkwMQwclz.txt', 'jiUjczNevXnhNaGpRKvkbQJnqDHspO.txt', 'MQNILUOnCMJrJJIoBPPGcTOdisXPPh.txt', 'RUPVgyakNwMArGHaswiXqwnCiNiCgf.txt', 'nLNzVbbkRTmSGQGGgEPGVRuexLRJyD.txt']
banstrin = 'YAPgtiVKGgYLLHkuzcuErNKjYlBBhS.txt'

dogrumu = False
print("Protection başlatılıyor.... Biraz uzun sürebilir...")

#try:
#    banden = requests.get(f"https://raw.githubusercontent.com/hayatyaw/hwid/main/{banstrin}")
#    if hwidAl() in banden.text:
#        DiscordWebhook(url=webhooklink, content=f"--------------\nBANLI GİRİŞ DENENDİ------------\nIP: {requests.get("https://api.ipify.org").text}\n HWID: {(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}\n---------------").execute()
#        quit()
#    else:
#        pass
#except Exception as e:
#DiscordWebhook(url=webhooklink, content=f"---------------\nHATA = {e}\n IP: {requests.get("https://api.ipify.org").text}\n------------").execute()


#for i in range(100):
#    if check_if_process_running("fiddler.exe") == True:
#        DiscordWebhook(url="https://discord.com/api/webhooks/1192890910002905240/Iunia8s55bk_vN93Q9QuWh0EUGciLolJGwRaG4bjgiKbnuZNQ5SJrgMhpO83sosIxz2y", content=f"FIDDLER DETECTED\nHWID: {(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}").execute()
#        quit()
#    if check_if_process_running("httpdebugger.exe") == True:
#        DiscordWebhook(url="https://discord.com/api/webhooks/1192890910002905240/Iunia8s55bk_vN93Q9QuWh0EUGciLolJGwRaG4bjgiKbnuZNQ5SJrgMhpO83sosIxz2y", content=f"HTTP DEBUGGER DETECTED = {{(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}}").execute()
#        quit()
#    istekatbir = requests.get(f"https://raw.githubusercontent.com/hayatyaw/hwid/main/{strin.pop()}")
#    if hwidAl() in istekatbir.text:
#        dogrumu = True
#    else:
#        pass

#-----os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))----#
#------print(hashlib.sha384((deneme.encode())).hexdigest())-------#

#if dogrumu == True:
#    print("Hoşgeldiniz.....")
#    DiscordWebhook(url=webhooklink, content=f"--------\nBAŞARILI GİRİŞ\n--------\nIP Adresi: {requests.get("https://api.ipify.org").text} ").execute()
#    time.sleep(3)
#elif dogrumu == False:
#    ipadresial = requests.get("https://api.ipify.org/")
#    DiscordWebhook(url=webhooklink, content=f"--------------\nHWID KAYIT\n--------------\nIP ADRESI: {ipadresial.text}\nHWID: {(os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode())))}\n---------------------").execute()
#    input("Kapatmak için entere basın...: ")
#    quit()

####### "   @ koymak için-pyautogui.hotkey("altright","q")  " #######

debugMode = True
#debugInput = input("Debug mode açılsın mı: ")
#if int(debugInput) == 1:
#    debugMode = True
#else:
#    debugMode = False

try:
    os.remove("acilmis_hesaplar.txt")
    if debugMode == True:
        print("DEBUG | TXT SİLİNDİ")
except Exception as e:
    if debugMode == True:
        print(e)
    else:
        pass

try:
    os.remove("temp.txt")
    if debugMode == True:
        print("DEBUG | TXT SİLİNDİ")
except Exception as e:
    if debugMode == True:
        print(e)
    else:
        pass

print(debugMode)
time.sleep(5)

acilanHesapSayisi = 0
bitirilenHesapSayisi = 0
#-----------definitations-------#
pyautogui.FAILSAFE = False

def biracheck():
    try:
        listebiruzunlukkontrol = pyautogui.locateAllOnScreen('birahayir.png', confidence=0.90)
        uzunlukdeneme = len(list(listebiruzunlukkontrol))
        if uzunlukdeneme == 1:
            aynenoyle = pyautogui.locateAllOnScreen('birahayir.png', confidence=0.90)
            bir = next(aynenoyle)
            birx = int(str(bir).split("left=")[1].split(",")[0]) + 30
            biry = int(str(bir).split("top=")[1].split(",")[0]) + 30
            pyautogui.click(birx, biry)
        elif uzunlukdeneme == 2:
            aynenoylebir = pyautogui.locateAllOnScreen('birahayir.png', confidence=0.90)
            biray = next(aynenoylebir)
            birayx = int(str(biray).split("left=")[1].split(",")[0]) + 30
            birayy = int(str(biray).split("top=")[1].split(",")[0]) + 30
            ikiay = next(aynenoylebir)
            ikiayx = int(str(ikiay).split("left=")[1].split(",")[0]) + 30
            ikiayy = int(str(ikiay).split("top=")[1].split(",")[0]) + 30
            pyautogui.click(birayx,birayy)
            pyautogui.click(ikiayx,ikiayy)
        elif uzunlukdeneme == 3:
            aynenoyleiki = pyautogui.locateAllOnScreen('birahayir.png', confidence=0.90)
            biraya = next(aynenoyleiki)
            birayax = int(str(biraya).split("left=")[1].split(",")[0]) + 30
            birayay = int(str(biraya).split("top=")[1].split(",")[0]) + 30
            ikiaya = next(aynenoyleiki)
            ikiayax = int(str(ikiaya).split("left=")[1].split(",")[0]) + 30
            ikiayay = int(str(ikiaya).split("top=")[1].split(",")[0]) + 30
            ucaya = next(aynenoyleiki)
            ucayax = int(str(ucaya).split("left=")[1].split(",")[0]) + 30
            ucayay = int(str(ucaya).split("top=")[1].split(",")[0]) + 30
            pyautogui.click(birayax,birayay)
            pyautogui.click(ikiayax,ikiayay)
            pyautogui.click(ucayax,ucayay)
        elif uzunlukdeneme == 4:
            aynenoyleuc = pyautogui.locateAllOnScreen('birahayir.png', confidence=0.90)
            biruc = next(aynenoyleuc)
            birucx = int(str(biruc).split("left=")[1].split(",")[0]) + 30
            birucy = int(str(biruc).split("top=")[1].split(",")[0]) + 30
            ikiuc = next(aynenoyleuc)
            ikiucx = int(str(ikiuc).split("left=")[1].split(",")[0]) + 30
            ikiucy = int(str(ikiuc).split("top=")[1].split(",")[0]) + 30
            ucuc = next(aynenoyleuc)
            ucucx = int(str(ucuc).split("left=")[1].split(",")[0]) + 30
            ucucy = int(str(ucuc).split("top=")[1].split(",")[0]) + 30
            dortuc = next(aynenoyleuc)
            dortucx = int(str(dortuc).split("left=")[1].split(",")[0]) + 30
            dortucy = int(str(dortuc).split("top=")[1].split(",")[0]) + 30
            pyautogui.click(birucx,birucy)
            pyautogui.click(ikiucx,ikiucy)
            pyautogui.click(ucucx,ucucy)
            pyautogui.click(dortucx,dortucy)
    except Exception as e:
        if debugMode == True:
            print(e)
        else:
            pass

def tikla(x,y):
    biracheck()
    pyautogui.leftClick(x,y)
    if debugMode == True:
        print(f"DEBUG | TIKLANDI {x} {y}")
    time.sleep(0.3)

def birasiztikla(x,y):
    pyautogui.leftClick(x,y)
    if debugMode == True:
        print(f"DEBUG | TIKLANDI {x} {y}")
    time.sleep(0.3)

def kackeretikla(x,y,sayi):
    for i in range(sayi):
        pyautogui.leftClick(x,y)
    if debugMode == True:
        print(f"DEBUG | {sayi} TIKLANDI {x} {y}")
    time.sleep(0.3)

def cifttikla(x,y):
    biracheck()
    pyautogui.click(x,y)
    time.sleep(0.1)
    pyautogui.click(x,y)
    if debugMode == True:
        print(f"DEBUG | ÇİFT TIKLANDI {x} {y}")
    time.sleep(0.3)

def yaz(yazi):
    pyautogui.write(yazi, interval=0.1)
    time.sleep(0.4)

def bas(tus):
    pyautogui.press(tus)
    time.sleep(0.2)

def surukle(x1,y1,x2,y2):
    pyautogui.moveTo(x1,y1)
    if debugMode == True:
        print(f"DEBUG | MOUSE KAYDIRMA İŞLEMİ (1): {x1} {y1} koordinatlarına kaydırıldı")
    time.sleep(0.2)
    pyautogui.dragTo(x2,y2, button="left", duration=1)
    if debugMode == True:
        print(f"DEBUG | MOUSE KAYDIRMA İŞLEMİ (2): {x2} {y2} koordinatlarına draglandı")
    time.sleep(0.2)

def uyu(sure):
    time.sleep(sure)
    if debugMode == True:
        print(f"DEBUG | SLEEP {sure}")

def sagtik(x,y):
    biracheck()
    pyautogui.rightClick(x,y)

def bosluk(sayi):
    time.sleep(0.2)
    for i in range(sayi):
        pyautogui.press("space")
        time.sleep(0.1)
    if debugMode == True:
        print(f"DEBUG | {sayi} KADAR SPACE BASILDI")

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def ekrankontrol():
    try:
        if len(list(pyautogui.locateAllOnScreen('4.png', confidence=0.90))) == 4:
            if debugMode == True:
                print("DEBUG | EKRAN KONTROL YAPILDI")
            else:
                pass
        else:
            quit()
    except:
        quit()

#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------OYUN FONKSIYONLARI------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#

def buyucusec():
    while True:
        tikla(822,659)
        try:
            if len(list(pyautogui.locateAllOnScreen("buyucu1.png", confidence=0.98))) == 1:
                break
            else:
                pass
        except:
            pass

def nickkoy():
    tikla(1415,742) #randomzar
    tikla(1352,745) #nick tikla
    pyautogui.hotkey("ctrl", "a")
    bas("backspace")
    yaz(random_char(8))
    tikla(1248,807)

def tabdegis(sayi):
    if sayi == 1:
        pyautogui.hotkey("ctrl","alt","right")
    if sayi == 2:
        pyautogui.hotkey("ctrl","alt","left")

def baslangiccan():
        birasiztikla(985,638)
        birasiztikla(827,945)
        birasiztikla(957,531)
        bosluk(30)
        bas("3")
        bas("2")
        bas("1")

#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#
#-------------------------------##-------------------------------##-------------------------------#

def botMenu():
    os.system("cls")
    def hesapsayisikontrol():
        print("[1] Kaç hesap istiyorsun: ")
        hesapSayisi = input()
        return hesapSayisi
    variableIki = hesapsayisikontrol()
    print("[2] Hesap mail domainleri ne olsun (örn: gmail.com): ")
    mailAdi = input()
    print("[3] Hesapların şifresi ne olsun: ")
    sifreAdi = input()
    print("Başlatılıyor... VDS'den çık.")
    time.sleep(6)
    #------Hesap Açma-------#
    os.system("cls")
    print("İşlem başlatıldı...")
    for i in range(int(variableIki)):
        try:
            degiskenBir = mailAdi.replace("@", "%40")
            randomMail = random_char(15)
            stringDeneme = f"https://passport.oasgames.com/index.php?m=register&callback=jQuery172012427824237660734_1703094732220&email={randomMail}@{degiskenBir}&pwd={sifreAdi}&sp_promote=gamebox.com&_=1703094764081"
            open("acilmis_hesaplar.txt", "a+").writelines(f"{randomMail}@{mailAdi}:{sifreAdi}\n")
            open("temp.txt", "a+").writelines(f"{randomMail}@{mailAdi}:{sifreAdi}\n")
            birinciIstek = requests.get(stringDeneme)
            if debugMode == True:
                print(birinciIstek.text)
            if '"status":"ok",' in birinciIstek.text:
                print(f"HESAP AÇILDI | {randomMail}@{mailAdi}:{sifreAdi}")
            else:
                print("Bir hata oluştu, hesap oluşturulamadı. Lütfen daha sonra tekrar deneyiniz...")
                print(birinciIstek.text)
                if debugMode == True:
                    open("debug.txt", "a+").writelines(birinciIstek.text + "\n")
                    time.sleep(60)
                    sys.quit()
        except Exception as e:
            print(e)

botMenu()
