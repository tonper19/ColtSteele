import requests

url = 'https://icanhazdadjoke.com'
response = requests.get(url, headers={'Accept': 'text/plain'})
print(response.text)
response = requests.get(url, headers={'Accept': 'application/json'})
print('*** This is a string:')
print(response.text)    # this is just a string
print('*** This is a dictionary:')
data = response.json()  # this returns a dictionary
print(data)
print(data['joke'])
