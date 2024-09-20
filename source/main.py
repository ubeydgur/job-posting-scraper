import requests
from bs4 import BeautifulSoup

url = "https://remote.co/remote-jobs/developer/"
website_url = "https://remote.co/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", class_="card bg-white m-0")
job_elements = results.find_all("a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")

search = "python"

for job_element in job_elements:
    title = job_element.find("span", class_="font-weight-bold larger").text
    if search in title.lower():
        company = job_element.find("p", class_="m-0 text-secondary").contents[0].replace("|", "").strip()
        tags = job_element.find_all("span", class_="badge badge-success")
        tag_list = [tag.text for tag in tags]
        publish_date = job_element.find("span", class_="float-right d-none d-md-inline text-secondary").text
        link = website_url + job_element["href"]
        
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Tags: {tag_list}")
        print(f"Publish Date: {publish_date}")
        print(f"Link: {link}\n")
