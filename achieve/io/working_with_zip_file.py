from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Khởi tạo trình duyệt (Ví dụ: Chrome)
driver = webdriver.Chrome()

url = "https://outlook.office.com/mail/"
driver.get(url)