from argus.lib.util import JsonAbleObject
from argus.models.item import Item

class Inventory(JsonAbleObject):

    def __init__(self, slots: int):
        self.slots = slots
        self.items = []

    def inv_items(self, action, item, cnt):
        action = action.lower()
        if self.slots >= len(self.items):
            if action not in ['add','del']:
                raise Exception("must add or del")
            if len(self.items) == 0 and action == 'add':
                item.amount = cnt
                self.items.append(item)
                return {"your_cup_overflowth":item.__dict__}
            for i,v in enumerate(self.items):
                if item._uuid == v._uuid:
                    print("CHALLENGE", item._uuid, item.name, "vs.", v._uuid, v.name)

                    #print("GOT:",item.name)
                    if action == 'add':
                        tot = self.items[i].amount + cnt
                        for c in range(0,cnt):
                            if item.amount < item._max:
                                item.amount += 1
                            else:
                                return {"slot_full" : {"allowed":item._max,"current":item.amount}}
                        del self.items[i]
                        self.items.append(item)
                        return {"added": item.__dict__}
                    if action == 'del':
                        item.amount = self.items[i].amount - cnt
                        del self.items[i]
                        self.items.append(item)
                        if self.items[i].amount <= 0:
                            del self.items[i]
                            return {"removed" : v.name}
            item.amount = cnt
            self.items.append(item)
            return {"new_added": item.__dict__}
