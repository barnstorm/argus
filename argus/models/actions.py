from argus.lib.serialize import JsonAbleObject
from random import randint
from math import ceil

class Test:
    def __init__(self):
        pass

    def _result(self,result,chance,score):
        return {"result" : result, "chance": chance, "score": score}

    @staticmethod
    def fate(chance):
        fate = randint(0,99)
        s_res = ceil(chance / 5)
        f_res = ceil(99 - chance / 5)
        if fate <= chance:
            if fate in range(0,s_res):
                if fate == 0:
                    return Test()._result("critical_success",chance,fate)
                else:
                    return Test()._result("special_success",chance,fate)
            else:
                dim = s_res * 4
                if fate in range(dim, chance):
                    return Test()._result("lesser_success", chance, fate)
                else:
                    return Test()._result("success", chance, fate)
        elif fate > chance:
            if fate in range(f_res * 4, 99):
                if fate == 99:
                    return Test()._result("critical_failure",chance,fate)
                else:
                    return Test()._result("special_failure", chance, fate)
            else:
                return Test()._result("failure", chance, fate)