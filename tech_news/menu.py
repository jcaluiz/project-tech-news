import sys
from tech_news.analyzer.ratings import top_5_categories


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
            break
        if int(option_number) < 6:
            input(option_choice)
        else:
            raise ValueError


# Requisitos 11 e 12
def analyzer_menu():
    option_number = input_choice()
    option_choice = option_choice_number(option_number)
    try:
        input_choice_number(option_number, option_choice)
    except ValueError:
        print("Opção inválida", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    analyzer_menu()
