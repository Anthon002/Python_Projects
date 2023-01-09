import datetime
import winsound
def alarm():
    alrmTim=input("Set Alarm\n Hrs/Min (seperate hrs and min by a backword slash) \n")
    l=alrmTim.split("/")
    hr=int(l[0])
    min=int(l[1])
    l1=input("Am or Pm")
    amPm=l1.lower()
    if(amPm=="pm"):
        hr+=12
    while(True):
        if(hr==datetime.datetime.now().hour and min==datetime.datetime.now().minute):
            print("Wake Up to Reality")
            winsound.PlaySound("C:\\Users\\HP\\Music\\September Remix.mp3",winsound.SND_FILENAME)
            break  
alarm()