import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)   # 200 means success
print(response.text)          # Raw content
print(response.json())        # JSON response as Python dict

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Hello World",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
