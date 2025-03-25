# LinkedIn Company Profile Scraping

# Objective:
Develop a Python script to extract publicly available company profile information from LinkedIn without using the official API or requiring authentication.

## Description:
Write a Python script that Accepts a LinkedIn company profile URL as input. Scrapes the following details from the company’s LinkedIn page:

* Company Name
* Industry
* Company Size
* Website URL
* Follower Count

Displays the extracted data in a structured format, and Saves the output in a JSON file.

## Technolgies used:
**Programming Language:** Python (3.x)
**Libraries Used:**
* requests for fetching web content
* BeautifulSoup or Scrapy for HTML parsing
* selenium to by pass authentication.

## Additional Considerations:
Used Selenium to by pass authentication and rendered content needs to be loaded.
As LinkedIn tracks the frequent requests, and has a strong anti webscraping policy, Implemented user-agent rotation to reduce detection risks.
