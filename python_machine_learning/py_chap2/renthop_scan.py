from py_chap2_source import *

r = requests.get('https://www.renthop.com/chicago-il/apartments-for-rent')
print(r.content)

soup = BeautifulSoup(r.content, "html.parser")
listing_divs = soup.select('div[class*=search-info]')
print(listing_divs)
