from head import show_head
from menu import main_menu
from create import create_item
from list import show_items
from update import update_item
from delete import delete_item
from export import export_items

items = []
load_head = 0

while True:
    if load_head != 1: show_head()
    load_head = 1
    
    menu_option = main_menu()

    if (menu_option == 1):
        new_item = create_item()
        items.append(new_item)
    elif (menu_option == 2):
        show_items(items)
    elif (menu_option == 3):
        update_item(items)
    elif (menu_option == 4):
        delete_item(items)
    elif (menu_option == 5):
        export_items(items)
    elif (menu_option == 6):
        print("\nFechando o programa. Bye\n")
        break