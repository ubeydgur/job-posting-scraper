# Job Posting Scraper

Scanning job postings on the remote.co website with `BeautifulSoup` and `Requests`, classifying them according to a certain keyword, and writing the incoming information to an `Excel` file.

- Job Posting Website: [remote.com](https://remote.co/remote-jobs/developer/)

## Features
- Enter the word you want to search for in the titles of job postings.
  
- `BeautifulSoup` scrape the Title, Company, Tags, Publish Date and Link of the desired job advertisement.
  
- This collected information is neatly exported to an `Excel` file.

## Dependencies

- [Requests](https://pypi.org/project/requests/)

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [Pandas](https://pandas.pydata.org/)

## Usage

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python main.py
    ```

3. Enter your search query when prompted.

4. View the results.
