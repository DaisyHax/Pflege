from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

# importing the requests library
import requests

# sending get request and saving the response as response object
r = requests.get('http://127.0.0.1:8000/pflege/')

# extracting data in json format
data = r.json()

print(data)

for i in data:
    print(i)
    idee=i['id']
    cn=i['time']
    dt=i['date']
    to=i['reciever']
    content=i['content']
    print(cn)
    print(dt)
    break


s1=datetime.now().strftime('%Y-%m-%d %H:%M')
s2=dt+" "+cn
print(s1)
print(s2)
if(s1==s2):
    print("Done")
    #requests.delete('http://127.0.0.1:8000/Pflege/?ide='+idee)
    usr = "bhalotia.tannu@gmail.com"
    pwd = "bhagalpur"
    driver = webdriver.Firefox()
    # or you can use Chrome(executable_path="/usr/bin/chromedriver")
    driver.get("http://www.facebook.org")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get("https://www.facebook.com/messages/t/mln.koushik")
    time.sleep(5)
    textAreaElem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div')
    textAreaElem.click()
    textAreaElem.send_keys(content)
    textAreaElem.send_keys(Keys.RETURN)
    time.sleep(1000)
