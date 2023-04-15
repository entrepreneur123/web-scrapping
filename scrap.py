from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.linkedin.com/jobs/search?keywords=backend&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
page = requests.get(url)


soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('section', class_="two-pane-serp-page__results-list")


with open('scraping.csv', 'w',encoding='utf8',newline="") as f:
    thewriter = writer(f)
    header = ['info','title','subtitle','titlelink','metadata','location','time']
    thewriter.writerow(header)
 

    for list in lists:
        titleui = list.find("ul",class_="jobs-search__results-list ")
        info = list.find('div',class_="base-search-card__info").text.replace("\n","")
        title= list.find('h3',class_="base-search-card__title").text.replace("\n","")
        subtitle=list.find('h4', class_="base-search-card__subtitle").text.replace("\n","")
        titlelink = list.find('a',class_="hidden-nested-link").text.replace("\n","")
        metadata = list.find('div', class_="base-search-card__metadata").text.replace("\n","")
        location=list.find('span', class_="job-search-card__location").text.replace("\n","")
        time = list.find('span',class_="job-search-card__listdate")
        if time is not None:
            time = time.text.replace("\n","")
        else:
            time ="unknown"
        main = [info,title,subtitle,titlelink,metadata,location,time]
        print(main)

    thewriter.writerow(main)

    f.flush()


