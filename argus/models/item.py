from argus.lib.util import JsonAbleObject
from uuid import uuid1



class Item(JsonAbleObject):
    """
    item types : {"attack"}
    """
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self._max = 0
        self._uuid = str(uuid1())
        self.rank = 0
        self.type = None

