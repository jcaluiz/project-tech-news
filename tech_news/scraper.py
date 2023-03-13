import requests
from time import sleep
from bs4 import BeautifulSoup
# import urllib3


# Requisito 1
def fetch(url):
    sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        web_request = requests.get(url, headers=headers, timeout=3)
        if web_request.status_code == 200:
            return web_request.text
        web_request.raise_for_status()
    except (
            requests.exceptions.Timeout,
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            ):
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    hrefs = soup.find_all("a", class_="cs-overlay-link")
    href_list = [href["href"] for href in hrefs]
    return href_list


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        href = soup.find("a", class_="next page-numbers")["href"]
        if html_content is None:
            return None
        return href
    except Exception:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    print(scrape_next_page_link(fetch("https://blog.betrybe.coma/")))
