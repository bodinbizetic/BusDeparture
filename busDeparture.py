"""
/brief Program gets next departure of some bus from official site of "GSP"
"""

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
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.minutes = []
        self.hour = 0
        self.getNext()
          
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
        /brief Funtion that is used to create list of all times
        /return Returns list of times in format hour:minutes
        """
        temp = []
        for i in self.minutes:
            temp += [self.hour + ":" + i]
        
        return temp


def main():
    e = BusStart()
    temp = e.departureTime()
    for i in temp:
        print(i)


if __name__ == "__main__":
    main()