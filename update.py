from utils import get_valid_option, get_positive_float, calculate_rectangle_area, calculate_triangle_area, generate_id

title = "\n-> MENU: Atualizar dado cadastrado <-\n"
cultures = ["Soja", "Milho"]
geometric_figures = ["Retângulo", "Triângulo"]
products = ["Nitrogênio", "Fósforo", "Potássio"]

def update_item(items):
    print(title)

    if len(items) == 0:
        print("\nNenhum item encontrado.")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    id_to_update = input("Digite o ID do item que deseja atualizar: ")
    item = next((i for i in items if i["id"] == id_to_update), None)

    if not item:
        print(f"\nNenhum item encontrado com o ID: {id_to_update}")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    print(f"Escolha a cultura? Valor atual: {cultures[item['culture_index'] - 1]}")

    for (index, culture) in enumerate(cultures, start=1):
        print(f"{index}. {culture}")

    culture = get_valid_option("\nDigite o número da opção desejada: ", cultures)

    print(f"\nEscolha a figura geométrica? Valor atual: {geometric_figures[item['geometric_figure_index'] - 1]}")

    for (index, geometric_figure) in enumerate(geometric_figures, start=1):
        print(f"{index}. {geometric_figure}")

    geometric_figure = get_valid_option("\nDigite o número da opção desejada: ", cultures)

    print(f"\nCerto. Agora precisamos calcular a área da figura geométrica escolhida: ({geometric_figures[geometric_figure - 1]})")

    base = get_positive_float(f"Digite a base do {geometric_figures[geometric_figure - 1].lower()} (em metros): ")
    heigth = get_positive_float(f"Digite a altura do {geometric_figures[geometric_figure - 1].lower()} (em metros): ")
    
    area = 0
    if geometric_figure == 1: 
        area = calculate_rectangle_area(base, heigth)
    elif geometric_figure == 2:
        area = calculate_triangle_area(base, heigth)

    print(f"\nA área do {geometric_figures[geometric_figure - 1].lower()} é {area:.2f} m².")
    print(f"\nEscolha qual produto será aplicado na cultura? Valor atual: {products[item['product_index'] - 1]}")

    for (index, product) in enumerate(products, start=1):
        print(f"{index}. {product}")

    product = get_valid_option("\nDigite o número da opção desejada: ", products)

    dosage_per_m2 = get_positive_float("\nDigite a dosagem por metro quadrado (em mL): ")
    number_of_rows = int(get_positive_float("Digite o número de ruas: "))

    area_per_row = area / number_of_rows
    ml_per_row = dosage_per_m2 * area_per_row
    total_ml = ml_per_row * number_of_rows
    total_liters = total_ml / 1000

    item.update({
         "culture_index": culture,
        "culture": cultures[culture - 1],
        "geometric_figure_index": geometric_figure,
        "geometric_figure": geometric_figures[geometric_figure - 1],
        "product_index": product,
        "product": products[product - 1],
        "area": area,
        "number_of_rows": number_of_rows,
        "area_per_row": area_per_row,
        "ml_per_row": ml_per_row,
        "total_ml": total_ml,
        "total_liters": total_liters
    })

    print("\nDados atualizados com sucesso.")
    input("Aperte qualquer tecla para voltar ao menu inicial\n")