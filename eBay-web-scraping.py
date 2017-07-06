# Web scraping for Daily Deal of eBay

# Importing the libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Addressing scraped website 
url = ("http://www.ebay.com/globaldeals")

# Getting the HTML detail of the page
req_url = uReq(url)
html_detail = req_url.read()
req_url.close()

# HTML parsing
page_soup = soup(html_detail, "html.parser")

# Grabbing each product
#containers = page_soup.findAll("div", {"class":"col"})
products = page_soup.find_all("div", {"class":"col"})

filename = "ebay_deal.csv"
f = open(filename, "w", encoding = "utf-8")
headers = "Brand, Discounted Price (IDR), Product Link\n"

f.write(headers)

for product in products:
    name_product = product.find_all("span", {"itemprop":"name"})
    brand = name_product[0].text
    
    dis_price_product = product.find_all("span", {"itemprop":"price"})
    discounted_price = dis_price_product[0].text
    discounted_price = discounted_price.replace("IDR","")
    discounted_price = discounted_price.replace(",", "")
        
    product_link = product.a["href"]
    
    f.write(brand + "," + discounted_price + "," + product_link + "\n")

f.close()