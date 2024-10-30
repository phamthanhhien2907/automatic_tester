import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')  # Đọc file config.ini từ thư mục gốc

        # Lấy đường dẫn đến ChromeDriver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path'] + "\\chromedriver.exe"  # Đảm bảo bao gồm file chromedriver.exe

        # Tạo Service cho WebDriver
        service = Service(driver_path)

        # Khởi tạo WebDriver (Chrome)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver