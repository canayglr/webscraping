import requests as req
from bs4 import BeautifulSoup as bs

url="https://boxofficeturkiye.com/hafta/detay/2023-32"
r=req.get(url)
soup= bs(r.content,"lxml")

filmtablosu= soup.find("table",attrs={"id":"WeeklyMovieData"}).select("tr")
# soup.find("table",attrs={"class":"ustcizgi"}).select("tr:nth-of-type(2)>td>table:nth-of-type(3) > tr")
# class değeri ustcizgi olan table altındaki 2.trnin altındaki td nni altındaki 3.table ın altındaki tr
for i in range(1,21):
    filmadi=filmtablosu[i].find("a",attrs={"class":"movie-link"}).get("title")
    toplamhasilat=filmtablosu[i].select("td:nth-of-type(8) > span")[0].text
    toplamseyirci=filmtablosu[i].select("td:nth-of-type(9)")[0].text
    print("Film Adi:{} \nHasilat: {} \nToplam Seyirci: {}".format(filmadi,toplamhasilat,toplamseyirci))
    print("-"*30)
