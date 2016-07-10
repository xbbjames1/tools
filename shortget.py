
from lxml import etree
from lxml.html import fromstring, tostring
from selenium.webdriver import PhantomJS
import json
import time
import urllib2


json_list = []
def get_data(url):
    browser = PhantomJS()
    browser.get(url)
    time.sleep(3)

    ul = browser.find_elements_by_xpath("//*[@id='ctl00_cph1_divSymbols']/table/tbody/tr/td[1]")
    tmp_list = []
    for e in ul:
        tmp_list.append(e.find_element_by_tag_name("a").text)
    
    json_list.append(tmp_list)
    print url[-5], "Done!"
    
    browser.close()

if __name__ == "__main__":
    BASE_DIR = "http://eoddata.com/stocklist/NYSE/"
    
    for i in range(ord('Z')-ord('A')+1):
        get_data(BASE_DIR+chr(i+ord('A'))+".htm")

with open("symbols.json","wb") as f:
        f.write(json.dumps(json_list,indent=2))
        f.close()



