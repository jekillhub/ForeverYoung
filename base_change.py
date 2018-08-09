class Changer:

    def any_to_decimal(self, number_in_base, base):
        exponent = 0
        decimal = 0
        for i in number_in_base:
            decimal += (base ** exponent) * int(i)
            exponent += 1
        return decimal

    def decimal_to_any(self, decimal, base):
        number_in_base = []
        while decimal > 0:
            number_in_base.append(str(decimal % base))
            decimal //= base
        return number_in_base

