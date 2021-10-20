from bs4.element import TemplateString
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_url="en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver")
browser.get(start_url)
time.sleep(10)
def scrape():
    headers=["v.mag","propername","bayer designation","distance","spectal class","mass","radius","luminosity"]
    planet_data=[]
    for i in range(0,454):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp=[]
            for index, li_tag in enumerate(li_tags):
                if (index==0):
                    temp.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp.append(li_tag.contents[0])
                    except:
                        temp.append("")
            planet_data.append(temp)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[1]/a').click()
    with open("scraper1.csv","w") as f:
        csv_writer= csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
scrape()                             