import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        web_request = requests.get(url, headers=headers, timeout=3)
        if web_request.status_code == 200:
            return web_request.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    print(fetch("https://blog.betrybe.com/"))
