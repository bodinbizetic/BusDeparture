"""
/brief Program gets next departure of some bus from official site of "GSP"
"""
#Idea for improvment: get links to buses automaticaly

import requests
from bs4 import BeautifulSoup
import datetime

class BusStart:
    """
    /brief Class that contains information of next departure of Bus
    /init Pass url to webpage of bus
    """
    def __init__(self, url="https://www.busevi.com/red-voznje/linija-eko-1-vukov-spomenik-naselje-belville/"):
        page = requests.get(url)
        self.url = url
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.minutes = []
        self.hour = 0
        self.getNext()

    def getReverseStation(self):
        """
        /brief Function that returns link for different orientation of bus
        /returns url link as string
        """
        links = self.soup.find_all(class_="vc_tta-tab")
        link = links[1].find('a')
        return self.url + link['href']

    def getNext(self):
        """
        /brief Function that scraps information about next departure of Bus
        """
        self.hour = self.soup.find(class_="row-2 even").find(class_="column-1").text
        dayOfWeek = datetime.datetime.today().weekday()
        if dayOfWeek<5:
            self.minutes = self.soup.find(class_="row-2 even").find(class_="column-2").text
        elif dayOfWeek == 5:
            self.minutes = self.soup.find(class_="row-2 even").find(class_="column-3").text
        elif dayOfWeek == 6:
            self.minutes = self.soup.find(class_="row-2 even").find(class_="column-4").text
        
        self.minutes = self.minutes.split(" ")

    def departureTime(self):
        """
        /brief Funtion that is used to create list of all timestamps of buses departure
        /return Returns list of times in format hour:minutes
        """
        temp = []
        for i in self.minutes:
            temp += [self.hour + ":" + i]
        
        return temp


def main():
    e = BusStart()
    temp = e.getReverseStation()
    print(temp)


if __name__ == "__main__":
    main()