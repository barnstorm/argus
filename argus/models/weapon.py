from argus.models.item import *

class Weapon(Item):

    def __init__(self,name, description, value, attack, damage):
        self.name = name
        self.description = description
        self.value = value
        self.attack = attack
        self.damage = damage
        self._max = 0
        self._uuid = str(uuid1())