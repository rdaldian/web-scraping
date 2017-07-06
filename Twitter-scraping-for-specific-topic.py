# Twitter Scraping or Crowling Using Beautiful Soup

# Importing the Libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Specifying the most recent tweet on Specific Topics
url = 'https://twitter.com/search?q=deep%20learning&src=tyah'

# Grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_html, "html.parser")

# Grabbing each product and Saving them to *.csv file
containers = page_soup.findAll("li", {"class":"js-stream-item stream-item stream-item "}) 

filename = "tweet_DL.csv"
f= open(filename, "w", encoding = "utf-8")
headers = "category, account, name, time, content, reply, retweet, favorite\n"
f.write(headers)

for container in containers:
    category = ("Deep Learning")
    
    account_container = container.findAll("span", {"class":"username u-dir"})
    account = account_container[0].text
    
    name_container = container.findAll("strong", {"class":"fullname show-popup-with-id "})
    name = name_container[0].text
    name = name.replace(",", " ")
    
    time_container = container.findAll("span", {"data-aria-label-part":"last"})
    time = time_container[0].text
    
    content_container = container.findAll("p", {"class":"TweetTextSize js-tweet-text tweet-text"})
    content = content_container[0].text
    content = content.replace(",", " ")
    content = content.replace("\n", " ")
    
    reply_container = container.findAll("span", {"class":"ProfileTweet-action--reply u-hiddenVisually"})
    reply = reply_container[0].text.replace("\n\n","")
    reply = reply.replace(" balasan", "")
    
    retweet_container = container.findAll("span", {"class":"ProfileTweet-action--retweet u-hiddenVisually"})
    retweet = retweet_container[0].text.replace("\n\n","")
    retweet = retweet.replace(" retweet", "")
    
    favorite_container = container.findAll("span", {"ProfileTweet-action--favorite u-hiddenVisually"})
    favorite = favorite_container[0].text.replace("\n\n","")
    favorite = favorite.replace(" suka", "")
    
    print("category: " + category)
    print("account: " + account)
    print("name: " + name)
    print("time: " + time)
    print("content: " + content)
    print("reply: " + reply)
    print("retweet: " + retweet)
    print("favorite: " + favorite)
    
    f.write(category + "," + account + "," + name + "," + time + "," + content + "," + reply + "," + retweet + "," + favorite + "\n") 

f.close()