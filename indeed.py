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

def extract_job(html):
    jobTitle = html.find("h2", {"class":"jobTitle"})
    title = jobTitle.find("span").string
    company = html.find("span", {"class":"companyName"}).string
    if title == "new":
        title = jobTitle.find_all("span")[1].string
    location = html.find("div", {"class":"companyLocation"}).text
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, "link":f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
      print(f"Scraping page {page}")
      result = requests.get(f"{URL}&start={page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("a",{"class":"fs-unmask"})
      for result in results:
          job = extract_job(result)
          jobs.append(job)
    return jobs

    