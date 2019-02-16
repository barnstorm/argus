from models.item import Item
from models.inventory import BaseInventory,EntityInventory
from models.weapon import Weapon

if __name__ == '__main__':
    gold = Item("gold","a single gold piece",1)
    gold._max = 6
    my_inv = EntityInventory(5)
    print(my_inv.inv_items('add',gold,4))
    print("THIS",my_inv)
    print(my_inv.inv_items('add',gold,3))
    print("SHOULD BE 7")
    print(my_inv)
    sword = Weapon("sword","a sword",1,6,9)
    sword._max = 2
    sword.type = 'attack'
    gun = Weapon("gun","a gun",21,6,9)
    gun._max = 1
    gun.type = 'attack'
    print(my_inv.inv_items('add',sword,2))
    print(my_inv.inv_items('add',gun,5))
    print("SHOULD BE 2")
    print(my_inv)
    print(my_inv.drop_random())
    print(my_inv.viable_equipment("attack",type_array=['attack']))
