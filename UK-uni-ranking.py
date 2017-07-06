# Top UK University League Tables and Rankings

# Importing the libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Addressing scraped website 
url = ("https://www.thecompleteuniversityguide.co.uk/league-tables/rankings")

# Getting the HTML of the page
req_url = uReq(url)
html_detail = req_url.read()
req_url.close()

# HTML parsing
page_soup = soup(html_detail, "html.parser")

# Grabbing each element in the website
rankings = page_soup.find_all("tr", {"class":"league-table-institution collapsed"})

filename = "UK_uni_ranking.csv"
f = open(filename, "w", encoding = "utf-8")
headers = "Position, University, Entry Standards, Student Satisfication, Research Quailty, Graduate Prospects, Overall Score\n"
f.write(headers)

for ranking in rankings:
    pos_ranking = ranking.find_all("td", {"class":"league-table-expand"})
    position = pos_ranking[0].text
    
    name_ranking = ranking.find_all("td", {"class":"league-table-institution-name "})
    name = name_ranking[0].text

    standard_ranking = ranking.find_all("td", {"class":"league-table-column-value"})
    entry_standard = standard_ranking[0].text
    entry_standard = entry_standard.replace("\r\n                                ", "")
    entry_standard = entry_standard.replace("\r\n\r\n\n", "")
    
    satisfication_ranking = ranking.find_all("td", {"class":"league-table-column-value"})
    student_satisfication = satisfication_ranking[1].text
    student_satisfication = student_satisfication.replace("\r\n                                ", "")
    student_satisfication = student_satisfication.replace("\r\n\r\n\n", "")
    
    quality_ranking = ranking.find_all("td", {"class":"league-table-column-value"})
    research_quality = quality_ranking[2].text
    research_quality = research_quality.replace("\r\n                                ", "")
    research_quality = research_quality.replace("\r\n\r\n\n", "")
    
    prospect_ranking = ranking.find_all("td", {"class":"league-table-column-value"})
    graduate_prospect = prospect_ranking[3].text
    graduate_prospect = graduate_prospect.replace("\r\n                                ", "")
    graduate_prospect = graduate_prospect.replace("\r\n\r\n\n", "")
    
    score_ranking = ranking.find_all("td", {"class":"league-table-column-value"})
    overall_score = score_ranking[4].text
    overall_score = overall_score.replace("\r\n                                ", "")
    overall_score = overall_score.replace("\r\n\r\n\n", "")
        
    
    f.write(position + "," + name + "," + entry_standard + "," + student_satisfication + "," + research_quality + "," + graduate_prospect + "," + overall_score + "\n")

f.close()