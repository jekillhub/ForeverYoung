from base_change import *


class Searcher:
    changer = Changer()

    def base_search(self, decimal, number_in_base):
        lower_limit = 10
        upper_limit = decimal - 1
        base = 0
        while upper_limit - lower_limit > 1 and base == 0:
            medium_point = (lower_limit + upper_limit) / 2
            candidate = self.changer.any_to_decimal(number_in_base, medium_point)
            if candidate == decimal:
                base = medium_point
            elif decimal < candidate:
                upper_limit = medium_point
            else:
                lower_limit = medium_point
        return base
