import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category
)


def input_choice():
    number = input(
        """"Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair."""
    )
    return number


def option_choice_number(number):
    try:
        if type(int(number)) == int and int(number) < 6:
            option_choice = {
                "0": "Digite quantas notícias serão buscadas:",
                "1": "Digite o título:",
                "2": "Digite a data no formato aaaa-mm-dd:",
                "3": "Digite a categoria:",
                "4": top_5_categories(),
                "5": exit
            }
            return option_choice[str(number)]
        else:
            return "6"
    except ValueError:
        return "6"


def input_choice_number(option_number, option_choice):
    while option_number:
        if option_number == "5":
            print("Encerrando script")
            break
        if int(option_number) < 6:
            insert_information = input(option_choice)
            return insert_information
        else:
            raise ValueError


def get_information_by_choice(option_number, arg):
    option_choice = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_category,
        "4": top_5_categories,
    }
    return option_choice[option_number](arg)


# Requisitos 11 e 12
def analyzer_menu():
    option_number = input_choice()
    option_choice = option_choice_number(option_number)
    try:
        arg = input_choice_number(option_number, option_choice)
        if arg:
            return get_information_by_choice(option_number, arg)
    except ValueError:
        print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    print(analyzer_menu())
