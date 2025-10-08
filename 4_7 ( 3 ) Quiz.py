import requests
import json

BASE_URL = "http://host1.open.uom.lk:8080"
ENDPOINT = "/api/products/"
URL = BASE_URL + ENDPOINT

try:
    response = requests.get(URL)
    
    response.raise_for_status() 

    data = response.json()

    product_list = data.get("data", [])

    total_products = len(product_list)

    print(total_products)

except requests.exceptions.RequestException as e:

  print(f"Error accessing the API: {e}")
except json.JSONDecodeError:

  print("Error: Could not decode JSON response.")
