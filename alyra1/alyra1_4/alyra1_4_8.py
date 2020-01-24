import datetime

max = "0xffffffff"

print("Nombre de secondes maximales codés sur 4 octets (décimale) : "+str(int(max, 16)))

init = datetime.datetime(1970, 1, 1)
maxDate = init + datetime.timedelta(seconds=int(max, 16))
print("Date maximale pouvant être exprimée à l'aide de 4 octets depuis le 01/01/1970 : "+str(maxDate))
