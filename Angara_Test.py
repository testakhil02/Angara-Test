from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Firefox()
#Open Angara website
driver.get("https://www.angara.in/")
driver.maximize_window()
driver.implicitly_wait(8)
#select_Ring_Catogery
driver.find_element(By.XPATH, "//*[@id='main-nav']/li[3]/a").click()
time.sleep(5)
#handel POPUP window
#def test_popup():
#    driver.get("")
#select_dimond_ring- Twin-Row Natural Diamond Swirl Infinity Link Ring
driver.find_element(By.XPATH, "//*[@id='gf-products']/div[1]/div/div[1]/a/img").click()
time.sleep(6)
#select_Stone_Quality
driver.find_element(By.XPATH, "//*[@id='swatch-option1']/div/fieldset/ul/li[2]/div/div[1]").click()
time.sleep(4)
#select_Carat_Weight
driver.find_element(By.XPATH, "//*[@id='swatch-option2']/div/fieldset/div/div/select")
time.sleep(4)
#select_Metal_Type
driver.find_element(By.XPATH, "//*[@id='swatch-option3']/div/fieldset/ul/li[4]/div/div[1]").click()
time.sleep(4)
#select_Ring_Size
driver.find_element(By.XPATH, "//*[@id='option-box-1tem1']/div[2]/span").click()
driver.find_element(By.XPATH, "//*[@id='option-box-1tem1']/div[2]/ul/li[5]/a").click()
time.sleep(4)
#select_Certificate_Add_On
driver.find_element(By.XPATH, "//*[@id='option-box-3tem1']/div[2]/label[1]/label").click()
time.sleep(4)
'''
#select_Quantity():
driver.find_element(By.XPATH, "//*[@id='plus-icon']").click() # to Increase the quantity of product.
driver.find_element(By.XPATH, "//*[@id='minus-icon']").click()  # to Decrease the quantity of product.
'''
#add_to_cart
driver.find_element(By.XPATH, "//*[@id='8818607358233-product-form-buttons-template--22776952520985__main']/div[3]").click()
time.sleep(8)
'''#Add a Note
driver.find_element(By.XPATH, "//*[@id='shopify-section-template--22776949571865__main']/section/div[3]/form/div[3]/div[3]/ul/li[1]/button").click()
driver.find_element(By.XPATH, "//*[@id='note']").send_keys('Send Bill And Warranty Card too')
time.sleep(4)
# Select Country
driver.find_element(By.XPATH, "//*[@id='shopify-section-template--22776949571865__main']/section/div[3]/form/div[3]/div[3]/ul/li[2]/button").click()

# Select Country
driver.find_element(By.XPATH, "//*[@id='address_country']").click()
time.sleep(2)
# Select Province
driver.find_element(By.XPATH, "//*[@id='address_province']").click()
driver.find_element(By.XPATH, "//*[@id='address_province']/option[35]").click()
time.sleep(2)
# Enter Pin Code
driver.find_element(By.XPATH, "//*[@id='address_zip']").send_keys('201010')
time.sleep(2)
# Enter Pin Code
driver.find_element(By.XPATH, "//*[@id='shipping-calculator']/div/div[4]/input").click()
'''
#Checkout the Items
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
time.sleep(4)
#In Contact - Enter Mobile or Email ID
driver.find_element(By.XPATH, "//*[@id='email']").send_keys('testakhil05@gmail.com')
time.sleep(4)
#Shipping Address
driver.find_element(By.XPATH, "//*[@id='Select0']").click()
time.sleep(4)
# Enter First Name
driver.find_element(By.XPATH, "//*[@id='TextField0']").send_keys('Akhil')
# Enter Last Name
driver.find_element(By.XPATH, "//*[@id='TextField1']").send_keys('Tiwari')
# Enter Address
driver.find_element(By.XPATH, "//*[@id='shipping-address1']").send_keys('muradnagar, Ghaziabad')
driver.find_element(By.XPATH, "//*[@id='shipping-address1-option-1']/span/mark").click()
#Apartment Number
driver.find_element(By.XPATH, "//*[@id='TextField2']").send_keys('342')
#Enter City
driver.find_element(By.XPATH, "//*[@id='TextField3']").send_keys('Ghaziabad')
#Select State
driver.find_element(By.XPATH, "//*[@id='Select1']").click()
driver.find_element(By.XPATH, "//*[@id='Select1']/option[35]").click()
#Enter PIN Code
# If it is not fetched by entering Address Line number -83
#driver.find_element(By.XPATH, "//*[@id='TextField4']").send_keys('201010')

#Enter Phone Number
driver.find_element(By.XPATH, "//*[@id='TextField5']").send_keys('6497338921')

'''#Discount 
driver.find_element(By.XPATH, "//*[@id='ReductionsInput0']").send_keys() #Enter the Discount Code
driver.find_element(By.XPATH, "//*[@id='Form1']/div[1]/div/button").click() #Click on Apply Discount Code
'''
#Click on Continue to shopping
driver.find_element(By.XPATH, "//*[@id='Form0']/div[1]/div/div/div[2]/div/div[2]/div[1]/button").click()
'''
#Change the Email
driver.find_element(By.XPATH, "//*[@id='checkout-main']/div/div/div/div/section/div/div[1]/div[2]/a/span").click()

#Change the Address
driver.find_element(By.XPATH, "//*[@id='checkout-main']/div/div/div/div/section/div/div[2]/div[2]/a/span").click()
time.sleep(4)
'''
#Continue to Payment
driver.find_element(By.XPATH, "//*[@id='Form2']/div[1]/div/div/div/div/div[2]/div[1]/button").click()
time.sleep(10)

#Pay Now
driver.find_element(By.XPATH, "//*[@id='Form5']/div[1]/div/div/div[2]/div[1]/div/button/span").click()
time.sleep(4)


driver.quit()


