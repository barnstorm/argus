from argus.lib.util import JsonAbleObject
from argus.models.inventory import BaseInventory
from uuid import uuid1

class Entity(JsonAbleObject):
    def __init__(self, name, description,hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self._uuid = str(uuid1())
        self.nick = name
        self.inventory = BaseInventory(5)
        self.rank = 0



    def is_alive(self):
        return self.hp > 0


