from base_change import *

class Searcher:

    changer = Changer()

    def base_search(self, decimal, number_in_base):
        lower_limit = 10
        upper_limit = decimal - 1
        medium_point = (lower_limit + upper_limit) / 2
        base = 0
        while lower_limit != medium_point and medium_point != upper_limit and base == 0:
            candidate_1 = self.changer.any_to_decimal(number_in_base, lower_limit)
            candidate_2 = self.changer.any_to_decimal(number_in_base, medium_point)
            candidate_3 = self.changer.any_to_decimal(number_in_base, upper_limit)
            if candidate_1 == decimal:
                base = lower_limit
            elif candidate_2 == decimal:
                base = medium_point
            elif candidate_3 == decimal:
                base = upper_limit
            elif decimal < candidate_2:
                upper_limit = medium_point
            elif candidate_2 < decimal:
                lower_limit = medium_point
            medium_point = (lower_limit + upper_limit) / 2
        return base
