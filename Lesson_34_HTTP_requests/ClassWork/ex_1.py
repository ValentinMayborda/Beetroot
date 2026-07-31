import requests


def download_image(image_url, file_name):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
            print(f"Image saved as {file_name}")
    else:
        print(f"Failed to download the image. Status code: {response.status_code}")

download_image("https://www.python.org/static/img/python-logo.png", "python_logo.png")
