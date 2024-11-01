import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://remote.co/remote-jobs/developer/"
website_url = "https://remote.co/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", class_="card bg-white m-0")
job_elements = results.find_all("a", class_="card m-0 border-left-0 border-right-0 border-top-0 border-bottom")

search = "senior"

title_list = []
company_list = []
tags_list = []
publish_date_list = []
link_list = []


for job_element in job_elements:
    title = job_element.find("span", class_="font-weight-bold larger").text
    
    if search in title.lower():
        #contents, allows to select html code by splitting it into parts.
        company = job_element.find("p", class_="m-0 text-secondary").contents[0].replace("|", "").strip()
        tags = job_element.find_all("span", class_="badge badge-success")
        tags_text = [tag.text for tag in tags]
        publish_date = job_element.find("span", class_="float-right d-none d-md-inline text-secondary").text
        link = website_url + job_element["href"]

        title_list.append(title)
        company_list.append(company)
        tags_list.append(tags_text)
        publish_date_list.append(publish_date)
        link_list.append(link)
        
        #print(f"Title: {title}")
        #print(f"Company: {company}")
        #print(f"Tags: {tags_text}")
        #print(f"Publish Date: {publish_date}")
        #print(f"Link: {link}\n")



d = {'Title':title_list, 'Company':company_list, 'Tags':tags_list, 'Publish Date':publish_date_list, 'Link':link_list}
df = pd.DataFrame(d)

df.to_excel("data/job-posting.xlsx", index=False)