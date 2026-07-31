import requests

# GET request
# response = requests.get('https://api.github.com/users/torvalds')
# print(response.status_code)  # 200
# print(response.headers['Content-Type'])
#
# user = response.json()
# print(user['name'])
# print(user['company'])
# print(user['public_repos'])


# POST request
# new_post = {
#     'title': 'My new post',
#     'body': 'This is the body of my new post',
#     'userId': 6
# }
#
# response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
# print(response.status_code)
# print(response.json())
# QUERY PARAMETERS
# params = {'userId': 6, '_limit': 5}
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
# print(response.url)
# print(response.json())
#
# headers = {
#     'Authorization': 'Bearer your_token_here',
#     'Accept': 'application/json',
#     'User-Agent': 'Your app name'
# }
#
# response = requests.get('https://api.example.com', headers=headers)
# response = requests.get('https://api.example.com/admin', auth=('username', 'password'))
# response = requests.get('https://api.example.com', timeout=5)


# response = requests.get('https://api.github.com/users/torvalds')
# print(response.elapsed)
# print(response.text)
# print(response.content)
# response.raise_for_status()

def safe_get(url: str) -> dict | None:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Request timed out: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None

data = safe_get("https://api.github.com/users/torvalds")
if data:
    print(data["name"])