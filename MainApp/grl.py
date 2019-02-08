import json 
import requests 

# getting actual BTC/USD rate from coinmarketcap.com
def price_btc():
	#getting current data about bitcoin and taking price from it
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
	# price_usd have a lot of numbers after point
	price_usd = float(r.json()[0]['price_usd'])
	# decreased to 2 numbers after point
	#price_usd = float("{0:.2f}".format(price_usd))
	return price_usd

# getting actual ETH/USD rate from coinmarketcap.com
def price_eth():
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
	price_usd = float(r.json()[0]['price_usd'])
	#price_usd = float("{0:.2f}".format(price_usd))
	return price_usd

# calculating costs in USD balances of user
def bal_usd(bal_btc, bal_eth):
	if bal_btc and bal_eth:
		balance_usd = float(bal_btc) * price_btc() + float(bal_eth) * price_eth()
		balance_usd = float("{0:.2f}".format(balance_usd))
		return balance_usd
	else:
		return 0