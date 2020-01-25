"""
Python web scrapping with BeautifulSoup example

Scrap a web page with request and BeautifulSoup and then
save the results into a csv file.
The page is safe to scrape as Colt Steele, the instructor,
help creating it.

AUTHOR
    Tony Perez

DATE
    25/01/2020

"""

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("web_scrapping_example.csv", "w") as f:
    csv_writer = writer (f)
    csv_writer.writerow(["title", "link", "date"])
    for article in articles:
        # get the blog title and url link from the "a" tag:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
