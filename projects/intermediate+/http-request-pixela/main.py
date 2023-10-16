import requests

USERNAME = "andrepennini123"
TOKEN = "\gsdf768sd7f9vds8vs09d8"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "reading1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_graph.text)
import datetime as dt

create_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": input("Quantas páginas você leu hoje? "),
}

response = requests.post(url=create_pixel, json=pixel_config, headers=headers)
print(response.text)

DAY = today # Trocar por qualquer dia nesse formato "%Y%m%d"

pixel_manipulation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DAY}"

put_config = {
    "quantity": "15"
}

# response = requests.put(url=pixel_manipulation, json=put_config, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_manipulation, headers=headers)
# print(response.text)