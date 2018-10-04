ip10systeemis=input("Palun sisesta ipv4 aadress: ") #küsib kasutajalt aadressi ja salvestab selle muutujana
baidid = ip10systeemis.split(".") #jupitab punkti kohalt aadressi ja lisab need juppidena järjendisse
kahendndBait = [] 
jarjendKahendidena=[]

'''
Defineerib funktsiooni, mis teisendab kümnendsüsteemis
sisestatud ip aadressi jupi ühtede ja nullide jadaks.
Samuti kontrollib läbi allpool defineeritud funktsiooni
baidi pikkust ja lisab vajalikud null bitid.
'''
def teisenda(bait):
    if bait/2==0:
        kontrolliPikkust(kahendndBait)
        yhendJarjend = "".join(kahendndBait)
        pahumPidiJarjend = yhendJarjend[::-1]
        jarjendKahendidena.append(pahumPidiJarjend)
        kahendndBait.clear()
        return jarjendKahendidena #die Ende
    elif bait%2==0:
        bait=bait/2
        kahendndBait.append("0")
        teisenda(bait)
    elif bait%2>0:
        bait=int(bait/2)
        kahendndBait.append("1")
        teisenda(bait)

'''
Defineerib funktsiooni, mis kontrollib, kas kahendsüsteemi teisendatud aadress on kaheksa kohaline
ja kui ei ole lisab ette niikaua nulle kuni pikkus on kaheksa.
'''
def kontrolliPikkust(jarjend):
    if len(jarjend)==8:
        return jarjend
    else:
        jarjend.append("0")
        kontrolliPikkust(jarjend)

'''
For tsükliga käivitab iga aadressi punktiga eraldatud osa
teisendava funktsiooni
'''
for i in range(len(baidid)):
    teisenda(int(baidid[i]))
        
print(jarjendKahendidena)