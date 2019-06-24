from price_adapter import PriceAdapter
from price_info import PriceInfo


class CanadianTireAdapter(PriceAdapter):

    def get_url(self, sku):
        return f'https://www.canadiantire.ca/ESB/PriceAvailability?SKU={sku}&Store=0133&Banner=CTR&' \
               f'isKiosk=FALSE&Language=E&_=1561079821077'

    def get_store(self):
        return 'Canadian Tire'

    def get_skus(self):
        return {
            '3992740': 'Pit Barrel Vertical Smoker',
            '0791241': 'Orion 14-16ft boat cover'
        }

    def get_headers(self):
        return CanadianTireAdapter.headers

    def to_price_info(self, data, sku, name):
        data = data[0]
        regular_price = data['Price']
        current_price = data["Promo"]["Price"] if 'Promo' in data else regular_price
        uom = 'EA'  # TODO?
        return PriceInfo(sku, name, regular_price, current_price, uom)
