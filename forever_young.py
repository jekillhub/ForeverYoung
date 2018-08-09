from base_search import *
from base_change import *


class Solver:

    searcher = Searcher()
    changer = Changer()

    def small_new_age(self, age, low):
        for i in range(low, 10001):
            possible_new_age = list(str(i)[::-1])
            if i == 10000:
                return "end"
            if self.searcher.base_search(age, possible_new_age) != 0:
                return self.searcher.base_search(age, possible_new_age)

    def small_base(self, age):
        for base in range(100000, 9, -1):
            age_in_base = self.changer.decimal_to_any(age, base)
            check = 1
            for digit in age_in_base:
                if int(digit) > 9:
                    check = 0
                    break
            if check:
                return base

    def forever_young(self, age, low):
        if low > 10000:
            return self.small_base(age)
        else:
            new_age = self.small_new_age(age, low)
            if new_age == "end":
                return self.small_base(age)
            else:
                return new_age
