import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

USERNAME = ""
TOKEN = ""

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"


# GRAPH CREATION DETAILS
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Walking",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# POSTING OF PIXELS

post_endpoint = f"{graph_endpoint}/{graph_config['id']}"

post_config = {
    "date": today,
    "quantity": "6.1"
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)


print(response.text)