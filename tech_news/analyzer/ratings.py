from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5}
    ]
    collection = get_collection()
    news = [new["_id"] for new in collection.aggregate(pipeline)]
    return news


if __name__ == "__main__":
    print(top_5_categories())
