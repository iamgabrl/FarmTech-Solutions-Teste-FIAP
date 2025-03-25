from utils import get_valid_option

title = "-> MENU: PRINCIPAL <-"
options = ["Cadastrar novo dado", "Listar dados cadastrados", "Atualizar dado cadastrado", "Remover dado cadastrado", "Exportar dados gerados (CSV)", "Sair"]

def main_menu():
    print(title, "\n")

    for (index, option) in enumerate(options, start=1):
        print(f"{index}. {option}")

    option_choosen = get_valid_option("\nDigite o número da opção desejada: ", options)
    return option_choosen