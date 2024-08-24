from InquirerPy import inquirer
from data import get_fruit_df
from bar_chart import get_bar_chart_app
from pizza_chart import get_pizza_chart_app
from tree_graph import get_tree_graph_app
from scatter_plot import get_scatter_plot_app


def menu():
    options = [
        "Gráfico de barras",
        "Gráfico de pizza",
        "Gráfico de árvores",
        "Gráfico de dispersão",
        "Dashboard",
        "Sair",
    ]

    choice = inquirer.select(
        message="Escolha uma opção",
        choices=options,
        default="Gráfico de barras",
    ).execute()

    if choice == "Gráfico de barras":
        get_bar_chart_app(dataframe=get_fruit_df())
    elif choice == "Gráfico de pizza":
        get_pizza_chart_app(dataframe=get_fruit_df())
    elif choice == "Gráfico de árvores":
        get_tree_graph_app(dataframe=get_fruit_df())
    elif choice == "Gráfico de dispersão":
        get_scatter_plot_app(dataframe=get_fruit_df())
    elif choice == "Dashboard":
        print("TODO: Implementar dashboard")
    elif choice == "Sair":
        print("Até mais!")
        exit()


if __name__ == "__main__":
    while True:
        menu()
