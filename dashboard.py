import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

USERNAME = ""
TOKEN = ""

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = f"https://pixe.la/@{USERNAME}"

user_params = {
    "displayName": "Jakeo",
    "gravatarIconEmail": "johlstrom@gmail.com",
    "timezone": "Europe/Stockholm",
    "pinnedGraphID": "graph0"
}

response = requests.put(url=pixela_endpoint, json=user_params, headers=headers)
print(response.text)