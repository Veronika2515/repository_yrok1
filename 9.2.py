import requests

response = requests.get("https://httpbin.org/get")
print(response.text)
print(f"Datatype - {type(response.text)}")