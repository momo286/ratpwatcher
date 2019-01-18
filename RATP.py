import requests
import  time
a="https://api-ratp.pierre-grimaud.fr/v3/schedules/bus/61/jean+jaures/A"


while True:
    print("=============== Prochains Bus===============")
    r = requests.get(a, verify=True)
    b=r.json()
    print(b["result"]["schedules"][0]["message"])
    print(b["result"]["schedules"][1]["message"])
    print("============================================")
    print("               ")
    time.sleep(60)






