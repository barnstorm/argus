from argus.lib.serialize import JsonAbleObject
from argus.models.inventory import BaseInventory
from argus.models.entity import Entity
from uuid import uuid1


class Player(Entity):
    def __init__(self, name, description,hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self._uuid = str(uuid1())
        self.nick = name
        self.inventory = BaseInventory(20)