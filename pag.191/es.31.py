zone_italia = {
    "Zona nord":0,
    "Zona centro":0,
    "Zona sud":0,
    "Zona isole":0
}

totale_fatturato = 0

for i in zone_italia:
    print("Inserisci il fatturato della" , i)
    fatturato_parziale = int(input())
    totale_fatturato += fatturato_parziale
    zone_italia[i] = fatturato_parziale

percentuale_fatturato = {}

for e in zone_italia:
    percentuale = (zone_italia[e]/totale_fatturato)*100
    percentuale_fatturato[e] = percentuale

print("la suddivisione del fatturato è" , zone_italia , "quella delle percentuali è" , percentuale_fatturato)



