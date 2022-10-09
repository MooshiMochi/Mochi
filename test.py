import ctypes
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

pool = ThreadPoolExecutor(1)

user32 = ctypes.windll.user32

driver_opts = Options()
driver_opts.add_argument("--headless")
driver_opts.add_argument("--window-size=1920,1080")
driver_opts.add_argument("--scrollbars=no")
driver_opts.add_argument("--disable-gpu")

driver = webdriver.ChromiumEdge(
    service=Service(EdgeChromiumDriverManager().install()),
    options=driver_opts,
)


driver.get("https://www.google.com")
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")
