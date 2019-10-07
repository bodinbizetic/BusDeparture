from bs4 import BeautifulSoup
import requests

class BusNumUrlNotFound(Exception):
    """
    /brief Exception that signals that search bus link cannot be found
    """
    pass

class BusUrl:
    """
    /brief Class that contains method for gaining BusUrl
    """
    def __init__(self):
        
        with open("busUrl.txt", "r") as page:
            self.soup = BeautifulSoup(page.read(), "html.parser")
    
    def getBusLink(self, num):
        link = self.soup.find_all(class_="vc_gitem-link")
        for tag in link:
            if tag["href"].find("linija-"+ num) != -1:
                return tag["href"]
        raise BusNumUrlNotFound
            
def main():
    b = BusUrl()
    #print(b.getBusLink("00."))
    
if __name__ == "__main__":
    main()