# TO DO is broken
# make a GUI for the scraper

from urllib.request import urlopen
from bs4 import BeautifulSoup



def scrape(url, folder):
    # htmldata = urlopen('https://www.geeksforgeeks.org/')
    htmldata = urlopen('https://unsplash.com/t/wallpapers')
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
  
    for item in images:
        #print(item['alt'])
        # print(name)
        name = item['alt']
        link = item['src']
        # print(name)
        with open('media/scraped/' + name.replace('/', '') + '.jpg', 'wb') as imgfile:
            im = requests.get(link)
            imgfile.write(im.content)
            
        print(link)
        print(f"\n")

if __name__ == "__main__":
    scrape()