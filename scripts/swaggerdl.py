# Download the ABS Data API Swagger JSON file from GitHub

import requests

# URL of the ABS Data API Swagger YAML file, provided by the Australian Bureau of Statistics
url = "https://raw.githubusercontent.com/apigovau/api-descriptions/gh-pages/abs/DataAPI.openapi.yaml"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    with open("swagger.yaml", "wb") as file:
        file.write(response.content)
    print("Swagger YAML downloaded successfully!")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
