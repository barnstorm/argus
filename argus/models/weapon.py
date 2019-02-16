from argus.models.item import *

class Weapon(Item):

    def __init__(self,name, description, value, attack):
        self.name = name
        self.description = description
        self.value = value
        self.attack = attack
        self.damage = None
        self._max = 0
        self._uuid = str(uuid1())

    def _damage(self):
        """
        Override this method
        :return:
        """
        self.damage = None
