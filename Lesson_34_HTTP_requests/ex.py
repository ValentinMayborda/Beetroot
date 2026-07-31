import requests


# Get запит

# response = requests.get('https://api.github.com/users/torvalds')
# print(response.status_code)
# print(response.headers)
#
# user= response.json()
# print(user['name'])
# print(user['company'])

#######################################################################################################
# POST запит
# new_post = {
#     'title': 'Valentyn_M',
#     "body": "My second post",
#     'userId': 6
# }
#
# new_post1 = {
#     'title': 'Valentyn_M',
#     "body": "My first post",
#     'userId': 6
# }
#
# response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post1)
#
# print(response.status_code)
# print(response.json())

###################################################################################################################
# params = {'userId': 6, "_limit":5}
# response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
# print(response.url)
# print(response.json())
# print(response.status_code)
#
# ###########################################################################################################
#
# headers = {
#     "Authorization": "Bearer your_token",
#     "Accept": "application/json",
#     "User-Agent" : "Mozilla/5.0"
#     }
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
# response = requests.get('https://jsonplaceholder.typicode.com/users', auth=(headers("username", 'password')))
# response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=5)


response = requests.get('https://api.github.com/users/torvalds')
print(response.elapsed)
print(response.text)
print(response.content)
response.raise_for_status()

def safe_get(url: str) -> dict | None:
    try:
        requests.get(url,timeout =5)
