import requests
import os

data = requests.get(
    url = "https://api.hypixel.net/skyblock/profile",
    params = {
        "key": "fc33b4fe-4516-4fc3-a34c-440e391d4713",
        "profile": "4c6e4545638e4c3e8f1d62b8e561b6ed"
    }
).json()

bank = (data['profile']['banking']['balance'])
round(bank, 1)

if not os.path.exists('X.txt'):
    with open('X.txt','w') as f:
        f.write('0')
with open('X.txt','r') as f:
    st = int(f.read())
    st+=1 
with open('X.txt','w') as f:
    f.write(str(st))

with open("bank.txt","a") as file:
    file.write(f"{st},{bank}\n")