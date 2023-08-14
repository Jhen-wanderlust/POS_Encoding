import pandas as pd
import header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time




chrome_options = Options()
chrome_options.add_argument("nwapp=C:/Users/Me/Documents/POS_OTC/win64/win64/TITANS_KRAKEN.exe")
driver = webdriver.Chrome("C:/Users/Me/Desktop/POS_Encoding/nwjs-sdk-v0.62.0-win-x64/nwjs-sdk-v0.62.0-win-x64/chromedriver",options=chrome_options)
driver.maximize_window()
val = 20 # in seconds
driver.implicitly_wait(val)


for f in range(len(header.Cashier_username)):
  
 time.sleep(3)
 # LOGIN (DOUBLE CHECK YUNG USER/CASHIER)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
 time.sleep(1)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(5)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col[2]/ion-item/div[1]/div/ion-input/input").send_keys(80)
 time.sleep(1)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[8]/ion-col/button[2]/span").click()
 time.sleep(2)
 driver.switch_to.alert.accept() 
 time.sleep(5)
 driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-security-code/ion-content/div[2]/ion-grid/ion-row[6]/ion-col/button/span").click()
 time.sleep(2)
 driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys(header.Cashier_username[f])
 driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys(header.password[f])
 time.sleep(1)
 element = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]")
 driver.execute_script("arguments[0].scrollIntoView(true);", element);
 time.sleep(3)

 driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true;    }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
 time.sleep(2)

 driver.execute_script("document.querySelectorAll('body > ion-app > ion-modal > div > numpad > ion-content > div.scroll-content > ion-item > div.item-inner > div > ion-input > input')[0].value= 5000;")
 time.sleep(2)
 driver.execute_script("document.querySelectorAll('body > ion-app > ion-modal > div > numpad > ion-content > div.scroll-content > div > ion-grid > ion-row:nth-child(5) > ion-col:nth-child(3) > button')[0].click();")
 time.sleep(2)

driver.quit()
