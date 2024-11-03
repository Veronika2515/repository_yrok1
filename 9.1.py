import requests

response = requests.get("https://httpbin.org/")
print(response.content)
print(f"Datatype - {type(response.content)}")