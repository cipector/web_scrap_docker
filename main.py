import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# from difflib import HtmlDiff
# import re
# from urllib.parse import urljoin
# import sys
# import certifi
# import urllib3
# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import pandas


http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)





    # Get data for website 1
    print("Getting data for website 1...")
    # response1 = requests.get(url1, verify=False)
    response1 = http.request("GET", url1)

    if response1.status != 200:
        print("Error: Website 1 could not be accessed.")
        return

    website1_data = response1.data
import scrapy
def main():


if __name__ == "__main__":
    main()