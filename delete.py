title = "\n-> MENU: Remover dado cadastrado <-\n"

def delete_item(items):
    print(title)

    if len(items) == 0:
        print("\nNenhum item encontrado.")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    id_to_update = input("Digite o ID do item que deseja remover: ")
    item = next((i for i in items if i["id"] == id_to_update), None)

    if not item:
        print(f"\nNenhum item encontrado com o ID: {id_to_update}")
        input("Aperte qualquer tecla para voltar ao menu inicial\n")
        return

    items.remove(item)

    print("\nDado removido com sucesso.")
    input("Aperte qualquer tecla para voltar ao menu inicial\n")