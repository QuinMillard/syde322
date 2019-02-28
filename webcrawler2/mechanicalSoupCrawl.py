import mechanicalsoup
import re

# Connect to duckduckgo
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.nike.com/ca/t/air-max-720-shoe-Vc2TZM")

# Display the results
# for link in browser.get_current_page().select('a.result__a'):
#     print(link.text, '->', link.attrs['href'])

htmlContents = str(browser.get_current_page().findAll(True))
p = re.compile('CAD.*.235')
a = p.findall(htmlContents)

print(a)