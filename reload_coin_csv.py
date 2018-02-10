from coinmarketcap import Market


def main():
    market = Markter()
    coins = [coin['id'] for coin in market.ticker(limit=0)]
    with open('./data/coins.csv', 'w') as f:
        for x in (coins):
            f.write(x+'\n')

if __name__ == '__main__':
    main()
