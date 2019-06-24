from price_adapter import PriceAdapter
from price_info import PriceInfo


class HomeDepotAdapter(PriceAdapter):

    def get_store(self):
        return 'Home Depot'

    def get_skus(self):
        return {
            '1001185011': 'Fairy Stone Vinyl Tile',
            '1001033627': 'Starry Light Vinyl Tile',
            '1001185008': 'Plains Cottonwood Vinyl Tile',
            '1000689258': 'Weber Smokey Mountain 18'
        }

    def get_url(self, sku):
        return f'https://www.homedepot.ca/homedepotcacommercewebservices/v2/homedepotca/products/{sku}/' \
               'localized/7051?fields=BASIC_SPA&lang=en'

    def to_price_info(self, data, sku, name):
        optimized_price = data['optimizedPrice']
        current_price = optimized_price['displayPrice']['value']
        regular_price = optimized_price['regprice']['value'] if 'regprice' in optimized_price else current_price
        uom = optimized_price['displayPrice']['unitOfMeasure']
        return PriceInfo(sku, name, regular_price, current_price, uom)
