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
products = page_soup.find_all("div", {"class":"col"})

for product in products:
    product_url = product.a["href"]
    
    req_url_product = uReq(product_url)
    html_detail_product = req_url_product.read()
    req_url_product.close()
    
    page_soup_product = soup(html_detail_product, "html.parser")
    
    sub_products = page_soup_product.find_all("div", {"id":"CenterPanelInternal"})
    
    filename = "ebay_deal_complete.csv"
    f = open(filename, "w", encoding = "utf-8")
    headers = "Brand, Discounted Price (IDR), Product Link\n"
    f.write(headers)
    
    for sub_product in sub_products:
            
        brand_product = sub_product.find_all("h1", {"itemprop":"name"})
        brand = brand_product[0].text
        brand = brand.replace("Details about  \xa0", "")
        
        condition_product = sub_product.find_all("div", {"itemprop":"itemCondition"})
        condition = condition_product[0].text
        
        offer_product = sub_product.find_all("h2", {"id":"subTitle"})
        offer = offer_product[0].text
        offer = offer.replace("\n\t\t\t\t", "")
        
        print(brand)
        print(condition)
        print(offer)
         
        f.write(brand.replace(",", " ") + "," + condition + "," + offer.replace(",", " ") + "\n")
    
    f.close()