import requests
url = 'https://api.pandascore.io/v2/your-endpoint'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get(url, headers=headers)
print(response.json())
