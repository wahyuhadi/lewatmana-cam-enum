import datetime
import requests


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


def predict(date):

    date = datetime.datetime.strptime(date, '%H%M%S') - datetime.timedelta(hours=0, minutes=5, seconds=0)
    return date.strftime("%H%M%S")
        # print (date.strftime("%H%M%S"))


def chekUrl(url) :
    res = requests.get(url)
    if res.status_code == 200 or len(res.text) > 381:
        print (url, "Link actived")


def main():
    link = input("Latest link vidio :")
    parsingLink(link)
    global dateenum
    global url
    global hours
    for i in range(40):
        dateenum = predict(dateenum)
        urls = url+"video"+hours+"_"+dateenum+".384.mp4"
        chekUrl(urls)
    


if  __name__ == "__main__":
    main()
    pass