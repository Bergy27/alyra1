#Récupérer les 10 derniers ordres à l’achat et à la vente sur bitmex et bitfinex. 
#- Sur quelle place de marché est-il le plus intéressant d’acheter 0.0001 bitcoin?
#- Sur quelle place de marché est-il le plus intéressant d’acheter 20 dollars de bitcoins

import requests

NMB_RESULT = 10

def calculate_weighted_average(prices, weight):
	weighted_sum=0
	for index, price in enumerate(prices):
		weighted_sum += price*weight[index]
	sum_weight = sum(weight)
	weighted_average = weighted_sum/sum_weight
	return weighted_average

def best_price_dollar_bitfinex(goal_dollar):
	current_dollar = 0

	quantity_buyed = []
	price_buyed = []

	resp = requests.get("https://api-pub.bitfinex.com/v2/book/tBTCUSD/P0")

	for ordre in resp.json():
		if ordre[2]>0:
			size_dollar = ordre[2]*ordre[0]
			if (goal_dollar-current_dollar)<size_dollar:
				quantity_buyed.append(goal_dollar-current_dollar)
				price_buyed.append(ordre[0])
				break
			else:
				quantity_buyed.append(size_dollar)
				price_buyed.append(ordre[0])
				current_dollar += size_dollar
	return calculate_weighted_average(price_buyed, quantity_buyed)


def best_price_btc_bitfinex(goal_BTC):
	current_BTC = 0

	quantity_buyed = []
	price_buyed = []

	resp = requests.get("https://api-pub.bitfinex.com/v2/book/tBTCUSD/P0")


	for ordre in resp.json():
		if ordre[2]>0:
			if (goal_BTC-current_BTC)<ordre[2]:
				quantity_buyed.append(goal_BTC-current_BTC)
				price_buyed.append(ordre[0])
				break
			else:
				quantity_buyed.append(ordre[2])
				price_buyed.append(ordre[0])
				current_BTC += ordre[2]
	return calculate_weighted_average(price_buyed, quantity_buyed)


def best_price_btc_bitmex(goal_BTC):
	current_BTC = 0

	quantity_buyed = []
	price_buyed = []

	resp = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBT&depth="+str(NMB_RESULT))

	for ordre in resp.json():
		if ordre["side"]=="Sell":
			size_btc = ordre["size"]/ordre["price"]
			if (goal_BTC-current_BTC)<size_btc:
				quantity_buyed.append(goal_BTC-current_BTC)
				price_buyed.append(ordre["price"])
				break
			else:
				quantity_buyed.append(size_btc)
				price_buyed.append(ordre["price"])
				current_BTC += size_btc
	return calculate_weighted_average(price_buyed, quantity_buyed)




def best_price_dollar_bitmex(goal_dollar):
	current_dollar = 0

	quantity_buyed = []
	price_buyed = []

	resp = requests.get("https://www.bitmex.com/api/v1/orderBook/L2?symbol=XBT&depth="+str(NMB_RESULT))

	for ordre in resp.json():
		if ordre["side"]=="Sell":
			if (goal_dollar-current_dollar)<ordre["size"]:
				quantity_buyed.append(goal_dollar-current_dollar)
				price_buyed.append(ordre["price"])
				break
			else:
				quantity_buyed.append(ordre["size"])
				price_buyed.append(ordre["price"])
				current_dollar += ordre["size"]
	return calculate_weighted_average(price_buyed, quantity_buyed)


goal_BTC = 0.0001
goal_dollar = 20


#BITFINEX
price_per_btc_for_btc = best_price_btc_bitfinex(goal_BTC)
price_per_btc_for_dollar = best_price_dollar_bitfinex(goal_dollar)
print("Sur bitfinex, pour acheter {} bitcoin, il faudra dépenser {}$ (soit {} par bitcoin)".format(goal_BTC, goal_BTC*price_per_btc_for_btc ,price_per_btc_for_btc))
print("Sur bitfinex, pour acheter {}$ de bitcoin, vous aurez {} bitcoin (soit {} par bitcoin)".format(goal_dollar, goal_dollar/price_per_btc_for_dollar, price_per_btc_for_dollar))

print("")

#BITMEX
price_per_btc_for_btc = best_price_btc_bitmex(goal_BTC)
price_per_btc_for_dollar = best_price_dollar_bitmex(goal_dollar)
print("Sur bitmex, pour acheter {} bitcoin, il faudra dépenser {}$ (soit {} par bitcoin)".format(goal_BTC, goal_BTC*price_per_btc_for_btc ,price_per_btc_for_btc))
print("Sur bitmex, pour acheter {}$ de bitcoin, vous aurez {} bitcoin (soit {} par bitcoin)".format(goal_dollar, goal_dollar/price_per_btc_for_dollar, price_per_btc_for_dollar))

