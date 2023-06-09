import requests
from time import sleep
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news
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
    soup = BeautifulSoup(html_content, "html.parser")
    time = re.search(r"\d+", soup.find("li", class_="meta-reading-time").text)
    div_text = soup.find("div", class_="entry-content")
    information_news = {
        "url": soup.find('link', {'rel': 'canonical'})["href"],
        "title": soup.find("h1", class_="entry-title").text.strip(),
        "timestamp": soup.find("li", class_="meta-date").text,
        "writer": soup.find("a", class_="url fn n").text,
        "reading_time": int(time.group()),
        "summary": div_text.find("p").text.strip(),
        "category": soup.find("span", class_="label").text,
    }
    return information_news


# Requisito 5
def get_tech_news(amount):
    response = "https://blog.betrybe.com/"
    links = scrape_updates(fetch(response))
    news = []
    iteration_times = 0
    for _ in range(int(amount)):
        iteration_times += 1
        news.append(scrape_news(fetch(links[iteration_times - 1])))
        if len(links) == iteration_times:
            iteration_times = 0
            response = scrape_next_page_link(fetch(response))
            sleep(1)
            fetch_request = fetch(response)
            requests.get(scrape_next_page_link(fetch_request))
            links = scrape_updates(fetch_request)
    create_news(news)
    return news


if __name__ == "__main__":
    print(get_tech_news(30))
