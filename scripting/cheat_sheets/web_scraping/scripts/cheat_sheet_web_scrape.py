# This cheat cheet defines some key functions and methods for web scraping

#%%
# use requests to download a web page
# here additional the content is stored to a file
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') 
res.raise_for_status()  # checks for any error status retrieving the page (eg 404)
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

#%%
# Selector passed to the select() method    Will match  .  .  .
soup.select('div')                          # All elements named <div>
soup.select('#author')                      # The element with an id attribute of author
soup.select('.notice')                      # All elements that use a CSS class attri- bute named notice
soup.select('div span')                     # All elements named <span> that are within an element named <div>
soup.select('div > span')                   # All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]')                  # All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]')         # All elements named <input> that have an attribute named type with value button

#%%
# Example parsing a file
import bs4
exampleFile = open('../resources/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'lxml') 
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
print()
pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

# based on above example searching for a dedicated class
# first with select
# %%
spanElem = exampleSoup.select('.slogan')
print(spanElem)

# second with findAll
for each_div in exampleSoup.findAll('p',{'class':'slogan'}):
    print(each_div)
# %%
