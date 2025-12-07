from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ---------------- SETUP ---------------- #
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# ---------------- FRONTEND URL ---------------- #
BASE_URL = os.environ.get("BASE_URL", "http://user-frontend-ci:5173")
driver.get(f"{BASE_URL}/login")
time.sleep(1)

# ---------------- LOGIN ---------------- #
login_here = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p.cursor-pointer:nth-child(2)")))
driver.execute_script("arguments[0].click();", login_here)
time.sleep(1)

email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
email_field.send_keys("test123@gmail.com")
password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
password_field.send_keys("12345678")

signin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-black")))
driver.execute_script("arguments[0].click();", signin_button)
print("Login completed!")
time.sleep(3)

# ---------------- CLICK MENU ITEMS ---------------- #
menu_items = ["HOME", "COLLECTION", "ABOUT", "CONTACT"]

for item in menu_items:
    menu_element = wait.until(EC.presence_of_element_located((By.XPATH, f"//p[normalize-space()='{item}']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", menu_element)
    driver.execute_script("arguments[0].click();", menu_element)
    print(f"Clicked menu item: {item}")
    time.sleep(1)

# ---------------- CLICK HOME AGAIN ---------------- #
home_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='HOME']")))
driver.execute_script("arguments[0].scrollIntoView(true);", home_menu)
driver.execute_script("arguments[0].click();", home_menu)
print("Clicked HOME again")
time.sleep(1)

# ---------------- CLICK PRODUCT IMAGE ---------------- #
image_element = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.my-10:nth-child(2) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
    )
)
driver.execute_script("arguments[0].scrollIntoView(true);", image_element)
driver.execute_script("arguments[0].click();", image_element)
print("Clicked product image")
time.sleep(1)

# ---------------- SELECT SIZE "M" ---------------- #
size_m_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div/button"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", size_m_button)
driver.execute_script("arguments[0].click();", size_m_button)
print("Selected size M")
time.sleep(1)

# ---------------- ADD TO CART ---------------- #
add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'ADD TO CART')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
driver.execute_script("arguments[0].click();", add_to_cart_button)
print("Added to cart")
time.sleep(1)

# ---------------- CLICK CART ICON ---------------- #
cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Cart']")))
driver.execute_script("arguments[0].click();", cart_icon)
print("Opened cart")
time.sleep(1)

# ---------------- PROCEED TO CHECKOUT ---------------- #
checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
driver.execute_script("arguments[0].click();", checkout_button)
print("Proceeded to checkout")
time.sleep(1)

# ---------------- PLACE ORDER ---------------- #
place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='PLACE ORDER']")))
driver.execute_script("arguments[0].scrollIntoView(true);", place_order_button)
driver.execute_script("arguments[0].click();", place_order_button)
print("Order placed successfully!")

driver.quit()
