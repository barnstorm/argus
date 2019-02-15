from models.item import Item
from models.inventory import Inventory

if __name__ == '__main__':
    gold = Item("gold","a single gold piece",1)
    gold._max = 6
    my_inv = Inventory(5)
    print(my_inv.inv_items('add',gold,4))
    print("THIS",my_inv)
    print(my_inv.inv_items('add',gold,3))
    print("SHOULD BE 7")
    print(my_inv)
    sword = Item("sword","a sword",1)
    sword._max = 2
    print(my_inv.inv_items('add',sword,2))
    print(my_inv.inv_items('add',sword,5))
    print("SHOULD BE 2")
    print(my_inv)
    for i in my_inv.items:
        if i.name == "sword":
            print(i)