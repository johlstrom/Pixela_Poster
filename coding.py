import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

USERNAME = "johlstrom"
TOKEN = "z3cMz7n#RICcIO3J"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# GRAPH CREATION DETAILS
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph0",
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# POSTING OF PIXELS

post_endpoint = f"{graph_endpoint}/{graph_config['id']}"

post_config = {
    "date": today,
    "quantity": "75"
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)