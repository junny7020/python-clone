import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "http://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  links = pagination.find_all("a")
  pages =[]
  # pages is a list of anchors in the soup of pagination
  for link in links[:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page
#   for n in range(max_page):
#     print(f"start={n*50}")


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a",{"class":"fs-unmask"})
    for result in results:
        jobTitle = result.find("h2", {"class":"jobTitle"})
        title = jobTitle.find("span").string

        if title == "new":
            title = jobTitle.find_all("span")[1].string
        print(title)
    return jobs

    