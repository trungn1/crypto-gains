from coinmarketcap import Market

class Coin:
    def __init__(self, name, buy_price, quantity, buy_currency='USD'):
        '''
        INITIALIZE:
            name (str): name of the coin bought
            buy_price (float) - the price per coin in any currency
            quantity(float) - the quantity bought
            buy_currency(STR) - the currency used to buy it
        '''
        market = Market()
        self.name = name
        self.buy_price = buy_price
        self.buy_currency = buy_currency
        self.quantity = quantity
        self.online_result = market.ticker(self.name)[0]
        self.now_price = self._get_price() 
        self.status_usd = self.now_price * self.quantity
        self.start_price_usd = self._convert_usd(self.buy_currency)

    def __repr__(self):
        return "This is a {} coin".format(self.name)

    def _get_price(self):
        new_price = float(self.online_result['price_usd'])
        return new_price

    def calculate_return(self):
        self.profit = (self.now_price - self.buy_price) * self.quantity
        print("Your account is at ${}".format(str(self.status)[:5]))
        self.percentage = (self.now_price * self.quantity) /(self.buy_price * self.quantity)
        print('This result in a gain/loss of {}%'.format(str(self.percentage)[:5]))
    
    def _convert_usd(self, currency):
        market = Market()
        if currency != 'USD':
            buy_price_USD = float(market.ticker(self.name)[0]['price_usd'])
        else:
            buy_price_USD = self.buy_price
        return buy_price_USD * self.quantity
