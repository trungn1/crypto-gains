from coinmarketcap import Market
import json
import pandas as pd
import time
from Coin import Coin
from sys import argv

market = Market()

def make_coin_obj(row):
    '''
    INPUT: row (row) - the row from a pandas dataframe
    OUTPUT: a Coin object that keeps track of all information
    '''
    name = row['COIN_NAME']
    quantity = float(row['BUY_QUANTITY'])
    buy_currency = row['BUY_CURRENCY']
    buy_price = float(row['BUY_PRICE'])
    coin = Coin(name=name, buy_price=buy_price,
                quantity=quantity, buy_currency=buy_currency)
    return coin


if __name__ == '__main__':

    col = ['COIN_NAME','coin_object','start','now']

    #loading in my buy data
    data_file = './data/buy_history.csv'
    with open(data_file) as f:
        df = pd.read_csv(f, encoding='utf-8')

    #collcecting new information
    df['coin_object'] = df.apply(lambda x: make_coin_obj(x), axis=1)
    df['start'] = df['coin_object'].apply(lambda x: x.start_price_usd)
    df['now'] = df['coin_object'].apply(lambda x: x.status_usd)

    #calculating metric
    account_value = round(df['now'].sum(),2)
    profit = round(df['now'].sum() - df['start'].sum(),2)
    profit_percent = round(df['now'].sum() / df['start'].sum(),2)

    #printing results
    if profit > 0:
        print("CONGRATULATIONS")
        print("Your account is worth ${}".format(str(account_value)))
        print("Your account is currently up +${}".format(str(profit)))
        print("Your account percentage gain is at {}%".format(str(profit_percent)))
    else:
        print("Don't cry but you are losing money right now ")
        print("Your account is worth ${}".format(str(account_value)))
        print("Your account is currently down -${}".format(str(profit)))
        print("Your account percentage loss is at {}%".format(str(profit_percent)))
