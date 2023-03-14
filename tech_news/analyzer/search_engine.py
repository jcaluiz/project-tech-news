from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search_list = search_news(query)
    tuple_search = []
    for search in search_list:
        tuple_search.append(
            (search["title"], search["url"])
        )
    return tuple_search


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    search_list = search_news(query)
    tuple_search = []
    for search in search_list:
        tuple_search.append(
            (search["title"], search["url"])
        )
    return tuple_search


if __name__ == "__main__":
    print(search_by_title("notícia"))
