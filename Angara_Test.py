import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver with options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Open browser in incognito mode
options.page_load_strategy = "eager"  # Load DOM faster
driver = webdriver.Chrome(options=options)

# Clear cache & cookies using Chrome DevTools Protocol (CDP)
driver.execute_cdp_cmd("Network.clearBrowserCache", {})
driver.execute_cdp_cmd("Network.clearBrowserCookies", {})

driver.maximize_window()
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 30)

# Function to wait and click
def wait_and_click(locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

# Function to wait and send keys
def wait_and_send_keys(locator, value):
    element = wait.until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(value)

# Open Angara website
driver.get("https://www.angara.in/")
time.sleep(20)
# Select Ring Category
wait_and_click((By.XPATH, "//a[@title='Rings']"))
time.sleep(5)
# Select Diamond Ring
wait_and_click((By.XPATH, "//a[normalize-space()='Solitaire Round Diamond Infinity Promise Ring']"))
time.sleep(2)
# Select Gemstone Quality
wait_and_click((By.XPATH, "//button[contains(@aria-label,'K, I3')]"))
time.sleep(2)
# Select Total Carat Weight
wait_and_click((By.XPATH, "//img[@alt='1/4 Carat']"))
time.sleep(2)
# Select Metal Type
wait_and_click((By.XPATH, "//button[@aria-label='14K White Gold']"))
time.sleep(2)
# Select Ring Size
wait_and_click((By.CSS_SELECTOR, "div[class='slick-slide slick-active'] div div button[aria-label='8']"))
time.sleep(2)
# Select Certificate Add-On
wait_and_click((By.XPATH, "//body/main/div/div/div/div/div/div[4]/div[1]/button[2]"))
time.sleep(2)
# Add to Cart
wait_and_click((By.XPATH, "//span[contains(@class,'flex gap-1 items-center justify-center text-xs desk:text-base')]"))
time.sleep(2)
# Add a Note
wait_and_send_keys((By.XPATH, "//textarea[@placeholder='Type your message']"), "Product is Good")
wait_and_click((By.XPATH, "//button[normalize-space()='Save']"))
time.sleep(2)
# Secure Checkout
wait_and_click((By.XPATH, "//span[normalize-space()='Secure Checkout']"))
time.sleep(2)
# Enter Contact Details
wait_and_send_keys((By.XPATH, "//input[@class='p-2 border border-grayscale w-full hide-number-input-arrows']"), "9876543210")
wait_and_send_keys((By.XPATH, "//input[contains(@type,'email')]"), "test@gmail.com")
time.sleep(2)
# Enter Name
wait_and_send_keys((By.XPATH, "//input[@name='firstName']"), "Aman")
wait_and_send_keys((By.XPATH, "//input[@name='lastName']"), "Aman")
time.sleep(2)
# Enter Address
wait_and_send_keys((By.XPATH, "//input[@name='addressLine1']"), "HN - 46, Gurgaon, Haryana")
time.sleep(2)
# Enter City
wait_and_send_keys((By.XPATH, "//input[@name='city']"), "Gurgaon")
time.sleep(2)
# Select State
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='state']")))
Select(dropdown).select_by_value("Haryana")
time.sleep(2)
# Enter PIN Code
wait_and_send_keys((By.XPATH, "//input[@name='postalCode']"), "201010")
time.sleep(2)
# Enter Phone Number
wait_and_send_keys((By.XPATH, "//input[@name='phoneNumber']"), "6497338921")
time.sleep(2)
# Continue to Payment
wait_and_click((By.XPATH, "//button[normalize-space()='Continue To Payment']"))
time.sleep(2)
# Close browser
driver.quit()
