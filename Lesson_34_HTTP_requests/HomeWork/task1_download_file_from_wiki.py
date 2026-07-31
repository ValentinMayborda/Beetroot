"""Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc. """

import requests

def download_file(url, file_name):
    try:

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        #print(response.status_code)
        #print(response.url)

        if response.status_code ==200:
            print(f"{file_name} downloaded from {response.url}")

            with open(file_name, 'wb') as file:
                file.write(response.content)

                print(f"Downloaded {file_name}")

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

download_file('https://en.wikipedia.org/robots.txt', 'robots.txt')