import datetime
import requests

from time import sleep
vidioId = 0


def parsingLink(link):
    global dateenum 
    dateenum = 0
    date = link.split("video") 
    global url
    global hours
    url = date[0]
    times = (date[1].split(".")[0].split("_"))
    hours = times[0]
    dateenum = times[1]


def enums(date):

    date = datetime.datetime.strptime(date, '%H%M%S') - datetime.timedelta(hours=0, minutes=5, seconds=0)
    return date.strftime("%H%M%S")
        # print (date.strftime("%H%M%S"))

def predict(date):

    date = datetime.datetime.strptime(date, '%H%M%S') + datetime.timedelta(hours=0, minutes=5, seconds=0)
    return date.strftime("%H%M%S")

def chekUrl(type, url) :
    if type == "enum":
        res = requests.get(url)
        if res.status_code == 200 or len(res.text) > 381:
            print ("ENUM : ", url, "Link actived")
    else :
        loop = True
        while loop is True:
            sleep(3)
            res = requests.get(url)
            if res.status_code == 200 or len(res.text) > 381:
                print ("Predict : ", url, "Link actived")
                loop = False


def main():
    link = input("Latest link vidio (link) : ")
    parsingLink(link)
    global dateenum
    global url
    global hours
    numlink = int(input("Total link enum (number) : "))



    print ("[+] Enumeration running !")
    dateenums = dateenum
    for i in range(numlink):

        dateenums = enums(dateenums)
        urls = url+"video"+hours+"_"+dateenums+".384.mp4"
        chekUrl("enum", urls)


    print ("\n[+] Predict link running  ........... ctrl+c to close")
    try:
        datepredics = dateenum

        while True:
            datepredics = predict(datepredics)
            urls = url+"video"+hours+"_"+datepredics+".384.mp4"
            chekUrl("predict", urls)
            
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass


if  __name__ == "__main__":
    main()
    pass