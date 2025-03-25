title = "\n-> MENU: Listar dados cadastrados <-\n"

def show_items(items):
    print(title)

    if len(items) == 0:
        print("Nenhum item encontrado.")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    for (index, item) in enumerate(items, start=1):
        print(f"ID: {item['id']}")
        print(f"Cultura: {item['culture']}")
        print(f"Produto: {item['product']}")
        print(f"Formato da área: {item['geometric_figure']}")
        print(f"Área total: {item['area']:.2f} m²")
        print(f"Número de ruas: {item['number_of_rows']}")
        print(f"Área por rua: {item['area_per_row']:.2f} m²")
        print(f"Consumo por rua: {item['ml_per_row']:.2f} mL")
        print(f"Total necessário: {item['total_ml']:.2f} mL ({item['total_liters']:.2f} litros)")
        print("=" * 50)

    input("\nAperte qualquer tecla para voltar ao menu inicial\n")

    