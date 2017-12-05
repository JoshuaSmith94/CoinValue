from coinmarketcap import Market
coinmarketcap = Market()
coins = coinmarketcap.ticker('', limit=0, convert='GBP')
print(coins)