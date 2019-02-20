from argus.lib.tdb import TdbObj
from argus.models.inventory import BaseInventory,EntityInventory
from uuid import uuid1

class Entity(TdbObj):
    def __init__(self, name, description,hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.uuid = str(uuid1())
        self.nick = name
        self.inventory = self._inventory(self.uuid)
        self.rank = 0

    def is_alive(self):
        return self.hp > 0

    def _inventory(self,fk):
        EntityInventory()

