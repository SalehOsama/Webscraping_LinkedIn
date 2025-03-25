from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random
import json


# List of User Agents for Rotation.
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    ]

# Choosing random user-agent.
user_agent = random.choice(USER_AGENTS)


# Setting Chrome configurations for automation.
chrome_options = Options()
chrome_options.add_argument("--incognito")                  # Runs Chrome in Incognito mode.
chrome_options.add_argument("--log-level=3")                # Suppress unnecessary info, to avoid slowdown.
chrome_options.add_argument('--headless')                   # Runs chrome in headless mode (No UI).
chrome_options.add_argument(f"--user-agent={user_agent}")   # use the randomly selected user-agent.


company_url = str(input("Enter the LinkedIn Company URL : "))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)    # Launch chrome
driver.get(company_url)       # passing URL to browser.
sleep(5)


# Handling Login pop-up (Requires no authorization).
driver.find_element(By.CLASS_NAME, "contextual-sign-in-modal__modal-dismiss-icon").click()

page_content = driver.page_source                             # Getting the HTML content from driver
soup = BeautifulSoup(page_content,"html.parser")      # Applying HTML parser on content


company_details = {}

# Extract company name.
company = soup.find('h1')
company_name = company.text.strip()
company_details["company_name"] = company_name      # Adding comany name to dictionary


company_info_box = soup.find('dl',class_ = 'mt-6')    # selecting box where company Iinformation is stored
company_info = company_info_box.find_all('dd', class_ ='font-sans px-0.25 text-md text-color-text break-words overflow-hidden')     # Finding the company informations.
#print(company_info)


com = []

# Extracting only text from company_info List (exclude HTML Part).
for ind_val in company_info:
     com.append(ind_val.text.strip())            # Appending company information text to com list
# print(com)


# Adding company details to dictionary.
company_details["industry"] = com[1]
company_details["company_size"] = com[2]
company_details["website"] = com[0].split('\n')[0]        #  Extract only the URL part.

# Extracting a follwer count.
followers = soup.find('h3').text.split()[-2].strip()      # Ectracting only numbers.
company_details["followers"] = followers


# Display console output.
print(f"Company Name: {company_details['company_name']}")
print(f"Industry: {company_details['industry']}")
print(f"Company Size: {company_details['company_size']}")
print(f"Website: {company_details['website']}")
print(f"Followers: {company_details['followers']}")


# Create a Json file (company_profile.json) and save data in Json format.
with open("company_profile.json", "w") as json_file:
     json.dump(company_details, json_file, indent=4)

