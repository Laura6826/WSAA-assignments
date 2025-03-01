import requests

def test_requests_module():
    url = 'https://api.github.com'
    response = requests.get(url)
    if response.status_code == 200:
        print("Success! The requests module is working correctly.")
    else:
        print("Something went wrong. Status code:", response.status_code)

test_requests_module()
