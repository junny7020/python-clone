import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("http://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")
spans =[]
# pages is a list of anchors in the soup of pagination
for page in pages:
  spans.append(page.find("span"))
print(spans[:-1])