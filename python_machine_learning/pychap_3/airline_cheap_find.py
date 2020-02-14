from pychap3_source import *
chromedriver_path = "chromedriver/chromedriver"
browser = webdriver.Chrome(chromedriver_path)

#Chicago to Montana flights
sats = 'https://www.google.com/travel/explore?tfs=CBkQAxooEgoyMDIwLTAzLTAxagwIAhIIL20vMDFfZDRyDAgEEggvbS8wNTBsOBooEgoyMDIwLTAzLTA3agwIBBIIL20vMDUwbDhyDAgCEggvbS8wMV9kNEABSAFSA1VTRHAB&curr=USD&gl=us&hl=en&authuser=0&origin=https%3A%2F%2Fwww.google.com&mvb=ChIJoWKc0WWYSUARrBqEuX24WMASEgnnNUrBw8FFQBGsGoS5fXddwA'

print(browser.get(sats))
