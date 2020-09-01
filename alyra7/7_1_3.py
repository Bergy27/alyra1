import requests

resp = requests.get("https://data.messari.io/api/v1/assets/bat/metrics")

prix_max = resp.json()["data"]["all_time_high"]["price"]
prix_act = resp.json()["data"]["market_data"]["price_usd"]
pourcentage_en_circulation = resp.json()["data"]["supply"]["circulating"]/resp.json()["data"]["supply"]["y_2050"]

print("Prix max - Prix actuel")
print(str(round(prix_max,4))+" - "+str(round(prix_act,4)))

print("Pourcentage de jetons en circulation à ce jour : ")
print(round(pourcentage_en_circulation*100,2))

