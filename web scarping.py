import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd

response = r.get("https://www.scrapethissite.com/pages/simple/")
pageSource = response.text
with open("PageSource.txt","w",encoding="utf-8") as f:
  f.write(pageSource)

  with open("PageSource.txt", "r") as f:
    sourceCode = f.read()
    s = bs(sourceCode, "html.parser")
    # s = s.prettify()
    countryData= {"CountryName":[],"Country Capital":[],"Country Population":[],"Country Area":[]}
    countryNames = s.find_all("h3", {"class": "country-name"})
    countryCapitals = s.find("span", {"class": "country-capital"})
    countryPopulation = s.find("span", {"class": "population"})
    countryArea = s.find("span", {"class": "county-area"})
    for i in range(len(countryNames)):
        countryData["country Name"].append(countryNames[i].text.strip())
        countryData["country Capital"].append(countryCapitals[i].text.strip())
        countryData["country Population"].append(countryPopulation.text.strip())
        countryData["country Area"].append(countryArea.text.strip())

    countryInfodf = pd.DataFrame(countryData)
    countryInfodf.to_csv("CountryInfo.csv", index=False)


