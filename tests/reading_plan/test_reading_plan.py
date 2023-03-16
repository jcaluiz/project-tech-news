from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch

mock_db = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
        "title": "noticia_0",
        "timestamp": "23/11/2020",
        "writer": "Escritor_0",
        "reading_time": 2,
        "summary": "Sumario da noticia_0",
        "category": "Categoria_0",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "writer": "Eu",
        "summary": "Algo muito bacana aconteceu",
        "reading_time": 4,
        "timestamp": "04/04/2021",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia bacana 2",
        "writer": "Você",
        "summary": "Algo muito bacana aconteceu de novo",
        "reading_time": 11,
        "timestamp": "07/04/2022",
        "category": "Novidades",
    },
]


def test_reading_plan_group_news():
    with patch("tech_news.analyzer.reading_plan.find_news") as find_news_mock:
        find_news_mock.return_value = mock_db
        group_news_mock = ReadingPlanService.group_news_for_available_time(10)

        assert len(group_news_mock["readable"]) == 1
        assert len(group_news_mock["unreadable"]) == 1
        assert group_news_mock["readable"][0]["unfilled_time"] == 4

        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(-1)
