# https://faun.pub/how-to-install-selenium-in-linux-e8928b2b709
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime
import time
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

domains = ["MusicOnline.org","example.com"]
dead = open("dead.txt","w")
for domain in domains:
  try:
    driver.get("http://{}".format(domain))
    time.sleep(3)
    driver.save_screenshot(".screenshot/{}_TEP.png".format(domain))
    dead.write(domain + "\n")
    dead.write(pytesseract.image_to_string(Image.open(".screenshot/{}_TEP.png".format(domain))) + "\n")
  except Exception as err:
    print(err)
dead.close()
    
