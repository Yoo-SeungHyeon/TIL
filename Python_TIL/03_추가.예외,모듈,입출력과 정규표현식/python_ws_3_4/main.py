import requests, json

def res_data(data):
    response = data.json()
    print(f"Name: {response['name']}")
    print(f"Username: {response['username']}")
    print(f"Email: {response['email']}")

data = requests.get('https://jsonplaceholder.typicode.com/users/1')
res_data(data)