import pandas as pd
import header
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
#run backend 
cmd = "Start C:\\Users\Me\\Desktop\\POS_Encoding\\runBackend.vbs" # change the dir path
os.system(cmd)

#run the application 
chrome_options = Options()
chrome_options.add_argument("nwapp=C:/Users/Me/Documents/POS_OTC/win64/win64/TITANS_KRAKEN.exe") # change DIR path nang Application 
driver = webdriver.Chrome("C:/Users/Me/Desktop/POS_Encoding/nwjs-sdk-v0.62.0-win-x64/nwjs-sdk-v0.62.0-win-x64/chromedriver",options=chrome_options)
driver.maximize_window()
val = 20 # in seconds
driver.implicitly_wait(val)

  
 

time.sleep(3)
# LOGIN (DOUBLE CHECK YUNG USER/CASHIER)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(Keys.BACKSPACE)
time.sleep(1)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[3]/ion-col/ion-item/div[1]/div/ion-input/input").send_keys(5)

driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[6]/ion-col[2]/ion-item/div[1]/div/ion-input/input").send_keys(80)
time.sleep(4)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-setup/ion-content/div[2]/form/ion-card/ion-grid/ion-row[11]/ion-col/button[2]").click()
#driver.execute_script("document.querySelectorAll('body > ion-app > ion-modal > div > page-setup > ion-content > div.scroll-content > form > ion-card > ion-grid > ion-row:nth-child(11) > ion-col > button:nth-child(2)')[0].click();")
time.sleep(4)
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card[2]/ion-list/ion-item[1]/div[1]/div/ion-input/input").send_keys('jilyn') #pwede dynamic
driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/ion-card[2]/ion-list/ion-item[2]/div[1]/div/ion-input/input").send_keys(1)
time.sleep(4)

driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/ion-grid/ion-row[1]/ion-col/form/div/button[1]").click()
time.sleep(4)
driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.button-inner')[index].innerText == 'CASH FUND'){find_element = true; }document.querySelectorAll('.button-inner')[index].innerText;index++;}if(find_element){document.querySelectorAll('.button-inner')[index-1].click();}")
time.sleep(2)
buttons = driver.find_elements_by_class_name('button.button-md.button-outline.button-outline-md.button-round.button-round-md.button-large.button-large-md')
time.sleep(1)
#hardcode since 5k lang naman lahat sa cashfund
buttons[4].click() #5
buttons[10].click() #0
buttons[10].click() #0
buttons[10].click() #0
time.sleep(2)
driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/numpad/ion-content/div[2]/div/ion-grid/ion-row[5]/ion-col[3]/button").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(30) #30 seconds kasi matagal ang QZ tray printer
#loop sa cashering
for f in range(len(header.Cashier_username)):
  #declaration of all elements location
 search_Item = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-otc/ion-content/div[2]/div/div[1]/div[1]/ion-grid/ion-row[1]/ion-col[1]/ion-searchbar/div/input")
 itembutton = driver.find_elements_by_class_name('itemmenu.button-md.item.item-block.item-md')
 qty = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/combo-picker/ion-content/div[2]/ion-grid/ion-row/ion-col[2]/ion-item/div[1]/div/ion-input/input")
 search_Price = driver.find_element_by_xpath("")
 #choose discount
 add_disc = driver.find_element_by_xpath("/html/body/ion-app/ng-component/ion-split-pane/ion-nav/page-otc/ion-content/div[2]/div/div[2]/ion-grid/ion-row/ion-col[5]/button")
 
 Senior_Citizen = 0 
 PWD = 1
 disc_10 = 2
 disc_20 = 3

 item1_discount_checkAll = driver.find_element_by_class_name("item1_discount")[0]
 card_name = driver.find_element_by_xpath("//*[@id='alert-input-3-0']")
 card_num = driver.find_element_by_xpath("//*[@id='alert-input-3-1']")
 
 paymentBtn= driver.find_element_by_class_name("colChild.button.button-md.button-default.button-default-md")
 #by class index since default naman lahat data
 cash = 12
 check = 13
 debit_card= 14
 credit_card= 15 
 gift_check= 16
 other_payment = 17
 
 otherPaymentBtn=driver.find_element_by_class_name("otherypayButton.button.button-md.button-outline.button-outline-md")
 #by class index since default naman lahat data
 gcash =0
 grabfood= 1
 shopeepay = 3

 #Start of all Actions 
 #sample item1 
 search_Item.send_keys(header.item1[f])
 time.sleep(2)
 search_Item.send_keys(Keys.ENTER)
 search_Price.send_keys(header.Price1[f])
 time.sleep(2)
 search_Price.send_keys(Keys.ENTER)
 time.sleep(2)
 itembutton[0].click()
 time.sleep(2)
 qty.clear()
 time.sleep(2)
 qty.send_keys(header.Item_qty1[f])
 time.sleep(2)
  #OTHERS per row
 sugarlevel1_ID = header.others_item1_sugarlevel1_ID[f]
 sugarlevel2_ID = header.others_item1_sugarlevel2_ID[f]
 otherAddOns_ID1 = header.others_item1_addons1_ID[f]
 otherAddOns_ID2 = header.others_item1_addons2_ID[f]
 otherAddOns_ID3 = header.others_item1_addons3_ID[f]
 #fire the Others per label
 driver.find_element_by_xpath("//*[contains(text(), '"+sugarlevel1_ID+"')]")
 time.sleep(2)
 driver.find_element_by_xpath("//*[contains(text(), '"+sugarlevel2_ID+"')]")
 time.sleep(2)
 driver.find_element_by_xpath("//*[contains(text(), '"+otherAddOns_ID1+"')]")
 time.sleep(2)
 driver.find_element_by_xpath("//*[contains(text(), '"+otherAddOns_ID2+"')]")
 time.sleep(2)
 driver.find_element_by_xpath("//*[contains(text(), '"+otherAddOns_ID3+"')]")
 time.sleep(2)

 add_disc.click()
 time.sleep(2)
 add_disc[header.Select_item1_discount_ID[f]].click()
 time.sleep(2)
 #confirm
 driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").click()
 time.sleep(2)
 Item_disc = header.item_item1_select_dic_ID
 if (header.Select_item1_discount_ID[f] =="Senior_Citizen"|"PWD"):
     if (Item_disc[f]== "Check_all"):
      driver.find_element_by_xpath("//*[@id='checkbox-281-0']").click()
      time.sleep(1)
      driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-otc-discount-per-item/ion-content/div[2]/div/div[2]/button").click()
     else:

         driver.find_element_by_xpath("//*[contains(text(), '"+Item_disc[f]+"')]").click()
         #Js script still testing 
         #driver.execute_script("var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[0].innerText.replace('\nD','') == Item_disc){find_element = true; }document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index].innerText;index++;}if(find_element){document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index-1].click();")
         time.sleep(1)
         driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-otc-discount-per-item/ion-content/div[2]/div/div[2]/button").click()
 else:
     False

 time.sleep(4)
 card_name.send_keys(header.Card_name_item1[f])
 time.sleep(1)
 card_num.send_keys(header.Card_number_item1[f])
 time.sleep(1)
 #confirm Discount
 driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").click()

 time.sleep(4)
 #payment input

 payment_Input = driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-otc-payment/ion-content/div[2]/div/div[1]/ion-grid/ion-row[2]/ion-col/ion-input/input")
 payment_Input.clear()
 time.sleep(4)
 payment_Input[header.amount[f]].click()
 time.sleep(4)
 #payment button
 paymentBtn[header.type_of_payment[f]].click()
 time.sleep(4)
 if (header.type_of_payment[f] =="other_payment"):
    # gcash /shopeepay/grabfood
   otherPaymentBtn[header.Other_payment_btn_ID[f]].click()
   time.sleep(4)
   driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").send_keys(header.reference_number_optional[f])
   time.sleep(3)
   driver.find_element_by_xpath("/html/body/ion-app/ion-modal[2]/div/page-otc-other-payments/ion-content/div[2]/button[1]").click()
   time.sleep(3)
 #confirm other payment
   driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").click()

 else:
 #confirm na 
  driver.find_element_by_xpath("/html/body/ion-app/ion-alert/div/div[4]/button[2]").click()
  time.sleep(4)
  driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-otc-payment/ion-header/ion-navbar/ion-buttons/button[2]").click()
  time.sleep(4)
  driver.switch_to.alert.accept()
  time.sleep(2)
  driver.switch_to.alert.accept()
  time.sleep(2)
  driver.switch_to.alert.accept()
  time.sleep(2)
  driver.find_element_by_xpath("/html/body/ion-app/ion-modal/div/page-otc-payment/ion-header/ion-navbar/ion-buttons/button[3]").click()
  time.sleep(4)



