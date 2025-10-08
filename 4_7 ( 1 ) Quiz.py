import requests
import json

BASE_URL = "http://host1.open.uom.lk:8080"
ENDPOINT = "/api/products/"
URL = BASE_URL + ENDPOINT

product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "CIC",
    "expiredDate": "2023.05.04",
    "manufactureDate": "2022.02.20",
    "batchNumber": "3243R",
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

try:
   
    response = requests.post(URL, json=product_data)

  print(response.status_code)

except requests.exceptions.RequestException as e:

print(f"An error occurred: {e}")
   
