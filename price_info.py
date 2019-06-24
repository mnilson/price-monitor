def __to_money__(val):
    return '${:,.2f}'.format(val)


class PriceInfo:

        def __init__(self, sku, name, regular_price, current_price, uom):
            self.sku = sku
            self.name = name
            self.regular_price = float(regular_price)
            self.current_price = float(current_price)
            self.uom = uom
            self.savings = regular_price - current_price

        def __repr__(self):
            return f'{self.sku}-{self.name} { __to_money__(self.current_price)} per {self.uom} ' \
                   f'Savings: { __to_money__(self.savings)}\n'
