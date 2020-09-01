import requests

resp = requests.get("https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD")
print("Le dernier échange sur bitfinex a été réalisé au prix de {} $/btc".format(str(resp.json()[0][7])))
