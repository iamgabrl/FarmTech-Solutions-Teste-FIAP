import csv

def export_items(items, file_name="data.csv"):
    if len(items) == 0:
        print("\nNenhum item encontrado.")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    fieldnames = items[0].keys()

    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

    print(f"\nDados exportados com sucesso para '{file_name}'!")
    input("Aperte qualquer tecla para voltar ao menu inicial\n")
