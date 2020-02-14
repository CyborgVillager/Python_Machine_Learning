from pychap3_source import *
chromedriver_path = "chromedriver/chromedriver"
browser = webdriver.Chrome(chromedriver_path)

#Chicago to Montana flights
sats = 'https://www.google.com/travel/explore?tfs=CBkQAxooEgoyMDIwLTAzLTAxagwIAhIIL20vMDFfZDRyDAgEEggvbS8wNTBsOBooEgoyMDIwLTAzLTA3agwIBBIIL20vMDUwbDhyDAgCEggvbS8wMV9kNEABSAFSA1VTRHAB&curr=USD&gl=us&hl=en&authuser=0&origin=https%3A%2F%2Fwww.google.com&mvb=ChIJoWKc0WWYSUARrBqEuX24WMASEgnnNUrBw8FFQBGsGoS5fXddwA'

print(browser.get(sats))
print(browser.title)

# will work on incrementing file names in the near future basic test

image_location = 'screenshot/'
img_name = 'flight_image_0'
file_format = '.png'
'''
img_number_counter = 0
img_name = 'flight_image_'
img_number_counter + 1
img_file_show = img_name + str(img_number_counter)

try:
    browser.save_screenshot(image_location + img_file_show + '.png')
    if img_number_counter <= 500:
        img_number_counter + 1
    else: print('Maxed out on picture space.')
except:
        print('Cant take screenshot at this time')

'''

try:
    browser.save_screenshot(image_location + img_name + file_format)
    print('Success, image is now saved @ folder screenshot. Saved as ' + img_name)
except OSError:
                print('Error cant save file ' + img_name + ' at this time' + 'please check the folder' + '\n' +
                      'screenshot')