import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="column is-half")

for job_element in job_elements:
    title_job = job_element.find("h2", class_="title is-5").text
    company_job = job_element.find("h3", class_="subtitle is-6 company").text
    location_job = job_element.find("p", class_="location").text.replace("\n", "").replace(" ", "")
    print(f"Title: {title_job}")
    print(f"Company: {company_job}")
    print(f"Location: {location_job}\n")
