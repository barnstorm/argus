from argus.lib.serialize import JsonAbleObject
from argus.models.item import Item

class BaseInventory(JsonAbleObject):

    def __init__(self, slots: int):
        self.slots = slots
        self._items = []
        self.uid = None

    def inv_items(self, action, item, cnt):
        action = action.lower()
        if self.slots >= len(self._items):
            if action not in ['add','del']:
                raise Exception("must add or del")
            if len(self._items) == 0 and action == 'add':
                item.amount = cnt
                self._items.append(item)
                return {"your_cup_overflowth":item.__dict__}
            for i,v in enumerate(self._items):
                if item._uuid == v._uuid:
                    print("CHALLENGE", item._uuid, item.name, "vs.", v._uuid, v.name)

                    #print("GOT:",item.name)
                    if action == 'add':
                        tot = self._items[i].amount + cnt
                        for c in range(0,cnt):
                            if item.amount < item._max:
                                item.amount += 1
                            else:
                                return {"slot_full" : {"allowed":item._max,"current":item.amount}}
                        del self._items[i]
                        self._items.append(item)
                        return {"added": item.__dict__}
                    if action == 'del':
                        item.amount = self._items[i].amount - cnt
                        del self._items[i]
                        self._items.append(item)
                        if self._items[i].amount <= 0:
                            del self._items[i]
                            return {"removed" : v.name}
            item.amount = cnt
            self._items.append(item)
            return {"new_added": item.__dict__}

    def drop_random(self):
        from random import randrange
        i = randrange(0, len(self._items))
        d = randrange(1, self._items[i].amount)
        ritem = self._items[i]
        item = self._items[i]
        ritem.amount -= d
        item.amount = d
        del self._items[i]
        self._items.append(ritem)
        return {"dropped": item.__dict__}

class EntityInventory(BaseInventory):
    def __init__(self,slots: int):
        self.slots = slots
        self._items = []
        self.attack_slots = 1
        self.attack_eqip = JsonAbleObject()
        self.defense_slots = 1
        self.defense_eqip = JsonAbleObject()

    def _viable_equipment(self,action,type_array=None,rank=0):
        options = []
        if type_array is None and action.lower() is "attack":
            type_array = ['attack','heal']
        if type_array is None and action.lower() is "defense":
            type_array = ['defend','evade']
        for i in self._items:
            if hasattr(i,"type"):
                if i.type in type_array:
                    print(i.name)
                    options.append(i.__dict__)
        return options



