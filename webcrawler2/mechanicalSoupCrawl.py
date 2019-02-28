import mechanicalsoup
import re
import smtplib
from email.message import EmailMessage

def crawl(siteurl, linkregex, shoeregex, imageregex, priceregex):
    browser = mechanicalsoup.StatefulBrowser()
    isOkay = browser.open(siteurl)

    badURL = []

    if str(isOkay) == '<Response [200]>':
        htmlContents = str(browser.get_current_page().findAll(True))

        links_to_search = re.compile(linkregex)
        links = links_to_search.findall(htmlContents)

        shoeList = []

        for link in links[:5]:
            isLinkOkay = browser.open(link)

            if str(isLinkOkay) != '<Response [200]>':
                badURLObj = { 'website': 'nike' , 'shoelink': link }
                badURL.append(badURLObj)
                continue

            htmlContents = str(browser.get_current_page().findAll(True))
            
            nike_price = re.compile(priceregex)
            price = nike_price.findall(htmlContents)

            nike_shoe = re.compile(shoeregex)
            shoe = nike_shoe.findall(htmlContents)

            nike_image = re.compile(imageregex)
            image = nike_image.findall(htmlContents)
            if(len(image) > 2 and len(price) > 0 and len(shoe) > 0):
                print(str(shoe[0]) + ', ' + str(price[0]) + ', ' + str(image[2]))
                shoeObj = { 'website': 'nike' ,'shoe' : shoe[0], 'price': price[0], 'imagelink': image[2], 'shoelink': link }
                shoeList.append(shoeObj)
            else:
                badURLObj = { 'website': 'nike' , 'shoe' : shoe, 'price': price, 'imagelink': image, 'shoelink': link }
                badURL.append(badURLObj)
    else:
        badURLObj = { 'website': 'nike' }
        badURL.append(badURLObj)

        
    if len(badURL) > 0:
        msg = EmailMessage()
        msg.set_content(str(badURL))

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'error with parser'
        msg['From'] = "quin.millard@gmail.com"
        msg['To'] = "quin.millard@gmail.com"

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()


    if len(shoeList) > 0:
        print('shoes!')
        # update database logic





storeLink = "https://store.nike.com/ca/en_gb/pw/mens-shoes/7puZoi3?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ASHOES&ipp=120"
getLinksRegex = r'\<a href\=\"([\w\:\/]*www\.nike\.com\/ca\/t\/[\w\d\/\-]*)\"\>'
getPriceRegex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
getShoeRegex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
getImageRegex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'

crawl(storeLink, getLinksRegex, getShoeRegex, getImageRegex, getPriceRegex)