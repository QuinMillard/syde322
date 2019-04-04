import mechanicalsoup
import re
import smtplib, ssl

def crawl(siteurl, linkregex, shoeregex, imageregex, priceregex):
    badURL = []
    shoeList = []
    browser = mechanicalsoup.StatefulBrowser()
   
    try:
        browser.open(siteurl)
        htmlContents = str(browser.get_current_page().findAll(True))

        links_to_search = re.compile(linkregex)
        links = links_to_search.findall(htmlContents)

        if len(links) == 0:
            badURLObj = { 'website': siteurl , 'error': "no relevent links found on site, consider updating regex"}
            badURL.append(badURLObj)

        for link in links[:5]:
            try:
                browser.open(link)
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

            except:
                badURLObj = { 'website': 'nike' , 'shoelink': link }
                badURL.append(badURLObj)
                
    except:
        badURLObj = { 'website': siteurl , 'error': "exception raised when opening site"}
        badURL.append(badURLObj)

        
    if len(badURL) > 0:
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = "swagifywebscrapererrors@gmail.com"
        receiver_email = "swagifywebscrapererrors@gmail.com"
        password = "syde322!"
        message = "There was an error scraping! \n" + str(badURL)
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit() 
        
        print(str(badURL))

    if len(shoeList) > 0:
        print('shoes!')
        # update database logic





storeLink = "https://store.nike.com/ca/en_gb/pw/mens-shoes/7puZoi3?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ASHOES&ipp=120"
getLinksRegex = r'\<a href\=\"([\w\:\/]*www\.nike\.com\/ca\/t\/[\w\d\/\-]*)\"\>'
getPriceRegex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
getShoeRegex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
getImageRegex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'

crawl(storeLink, getLinksRegex, getShoeRegex, getImageRegex, getPriceRegex)

# working cases for nikes
# storeLink = "https://store.nike.com/ca/en_gb/pw/mens-shoes/7puZoi3?intpromo=MLP-MEN%3ATOPNAV%3ASU18%3AMNSXCAT%3ASHOPMEN%3ASHOES&ipp=120"
# getLinksRegex = r'\<a href\=\"([\w\:\/]*www\.nike\.com\/ca\/t\/[\w\d\/\-]*)\"\>'
# getPriceRegex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
# getShoeRegex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
# getImageRegex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'

# does this crawler follow friendly crawling practices? by the friendly crawling standardization