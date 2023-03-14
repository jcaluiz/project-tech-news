from tech_news.database import search_news
from datetime import datetime


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
    tuple_search = []
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_iso = date_obj.strftime("%d/%m/%Y")
        query = {"timestamp": {"$regex": date_iso, "$options": "i"}}
        search_list = search_news(query)
        for search in search_list:
            tuple_search.append(
                (search["title"], search["url"])
            )
    except ValueError:
        raise ValueError("Data inválida")
    return tuple_search


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
    print(search_by_date("2022/04/07"))
