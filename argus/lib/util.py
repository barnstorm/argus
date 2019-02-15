import json


class JsonAble(json.JSONEncoder):

    def default(self, obj):
        try:
            return obj.__dict__
        except:
            return str(obj)

    @classmethod
    def create(cls, obj_dict : dict):
        c = cls()
        for k,v in obj_dict.items():
            k = k.replace("-", "_")
            if isinstance(v, dict):
                obj = JsonAbleObject.create(v)
                setattr(c, k, obj)
            elif isinstance(v, list):
                a_list = []
                setattr(c, k, a_list)
                for item in v:
                    if isinstance(item, dict):
                        obj = JsonAbleObject.create(item)
                        a_list.append(obj)
                    else:
                        a_list.append(item)
            else:
                setattr(c, k, v)
        return c
#
    def to_json(self):
        return json.dumps(self.__dict__, cls=JsonAble)
#
    def __str__(self):
        return json.dumps(self.__dict__, cls=JsonAble)
#
    def __getitem__(self, item):
        return getattr(self, item)
#
class JsonAbleObject(JsonAble):
      def __init__(self):
              pass
