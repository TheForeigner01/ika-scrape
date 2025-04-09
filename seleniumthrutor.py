from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time, random
import ikaWorld

    # Set up Firefox options to route traffic through Tor
firefox_options = Options()
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.socks", "127.0.0.1")
firefox_options.set_preference("network.proxy.socks_port", 9150)
firefox_options.set_preference("network.proxy.socks_remote_dns", True)  # Route DNS through Tor
#firefox_options.add_argument("--headless=new")

driver = webdriver.Firefox( options=firefox_options)

# Test if IP has changed by accessing a website
driver.get("https://check.torproject.org/")

#print(driver.title)  # This should show "Congratulations. This browser is configured to use Tor."

# Optionally, you could print the entire page's HTML
#print(driver.page_source)

ikaWorld.getDriver(driver)

world_view_url = "https://s305-en.ikariam.gameforge.com/?view=worldmap_iso"
driver.get(world_view_url)
driver.add_cookie({"name": "ikariam", "value": "159366_a1e4cb6e21ba7cbbef84972ee304bc12"}) #159366_2f26a03840fb2a00c76bc2ec2055af12
#ikaWorld.scrape_island(50,50)

input()