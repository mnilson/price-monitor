class PriceAdapter:
    headers = {'Accept': 'application/json,text/javascript,*/*',
               'Accept-Language': 'en',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/74.0.3729.157 Safari/537.36'
               }

    def get_store(self):
        return None

    def get_skus(self):
        return None

    def get_url(self, sku):
        return None

    def get_name(self, sku):
        return self.get_skus()[sku]

    def get_headers(self):
        return PriceAdapter.headers

    def to_price_info(self, data, sku, name):
        return None
