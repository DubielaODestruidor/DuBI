from InquirerPy import inquirer
from data import get_fruit_df
from bar_chart import get_bar_chart_app
from pizza_chart import get_pizza_chart_app
from tree_graph import get_tree_graph_app
from scatter_plot import get_scatter_plot_app


def center_text_with_dashes(text, total_width):
    text_length = len(text)
    if text_length >= total_width - 2:
        return f"-{text}-"

    total_spaces = total_width - text_length - 2
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return f"-{' ' * left_spaces}{text}{' ' * right_spaces}-"


def menu():
    options = [
        "Gráfico de barras",
        "Gráfico de pizza",
        "Gráfico de árvores",
        "Gráfico de dispersão",
        "Dashboard",
        "Sair",
    ]

    max_width = 25
    centered_options = [
        center_text_with_dashes(option, max_width) for option in options
    ]

    choice = inquirer.select(
        message="Escolha uma opção ('Ctrl'+'C' para sair): ",
        choices=centered_options,
        default=centered_options[0],
    ).execute()

    if "Gráfico de barras" in choice:
        get_bar_chart_app(dataframe=get_fruit_df())
    elif "Gráfico de pizza" in choice:
        get_pizza_chart_app(dataframe=get_fruit_df())
    elif "Gráfico de árvores" in choice:
        get_tree_graph_app(dataframe=get_fruit_df())
    elif "Gráfico de dispersão" in choice:
        get_scatter_plot_app(dataframe=get_fruit_df())
    elif "Dashboard" in choice:
        print("TODO: Implementar dashboard")
    elif "Sair" in choice:
        print("Até mais!")
        exit()


if __name__ == "__main__":
    while True:
        menu()
