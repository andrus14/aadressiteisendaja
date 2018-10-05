ip10systeemis = input("Palun sisesta ipv4 aadress: ")  # küsib kasutajalt aadressi ja salvestab selle muutujana
baidid = ip10systeemis.split(".")  # jupitab punkti kohalt aadressi ja lisab need juppidena järjendisse
kahendndBait = []
jarjendKahendidena = []

'''
Defineerib funktsiooni, mis teisendab kümnendsüsteemis
sisestatud ip aadressi jupi ühtede ja nullide jadaks.
Samuti kontrollib läbi allpool defineeritud funktsiooni
baidi pikkust ja lisab vajalikud null bitid.
'''

def teisenda(bait):
    if bait / 2 == 0:
        yhendJarjend = "".join(kahendndBait).zfill(8)
        pahumPidiJarjend = yhendJarjend[::-1]
        jarjendKahendidena.append(pahumPidiJarjend)
        kahendndBait.clear()
        return jarjendKahendidena  # die Ende
    elif bait % 2 == 0:
        bait = bait / 2
        kahendndBait.append("0")
        teisenda(bait)
    elif bait % 2 > 0:
        bait = int(bait / 2)
        kahendndBait.append("1")
        teisenda(bait)


'''
For tsükliga käivitab iga aadressi punktiga eraldatud osa
teisendava funktsiooni
'''
for i in range(len(baidid)):
    teisenda(int(baidid[i]))

print(jarjendKahendidena)