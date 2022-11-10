import requests


get_status = requests.get('https://google.com')
print(get_status.status_code)