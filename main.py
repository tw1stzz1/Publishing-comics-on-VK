import requests
import os
import random

from dotenv import load_dotenv


def get_comics_image():
    url = 'https://xkcd.com/353/info.0.json'
    response = requests.get(url)
    response.raise_for_status()

    image = response.json()['img']
    filename = response.json()['safe_title']
    alt = response.json()['alt']
    return image, filename, alt


def download_image(image_url, file_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_upload_url(vk_access_token, group_id):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "group_id" : group_id,
        "access_token" : vk_access_token,
        "v" : 5.131
    }
    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_comics(upload_url, comics_filepath):
    with open(comics_filepath, 'rb') as file:
        url = upload_url
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
    response.raise_for_status() 
    photo = response.json()['photo']
    server = response.json()['server']
    hash = response.json()['hash']
    return photo, server, hash

def upload_comics_on_wall(vk_access_token, group_id, photo, vk_server, hash):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token" : vk_access_token,
        "group_id" : group_id,
        "photo" : photo,
        "server" : vk_server,
        "hash" : hash,
        "v" : 5.131
    }
    response = requests.post(url, params)
    response.raise_for_status()
    media_id = response.json()['response'][0]['id']
    owner_id = response.json()['response'][0]['owner_id']
    return media_id, owner_id


def publsih_comics_on_wall(vk_access_token, group_id, client_id, owner_id, alt, media_id):
    url = "https://api.vk.com/method/wall.post"
    media_type = "photo"
    attachments = f"{media_type}{owner_id}_{media_id}" 
    params = {
        "access_token" : vk_access_token,
        "owner_id" : f"-{group_id}",
        "from_group" : 1,
        "attachments" : attachments,
        "message" : alt,
        "v" : 5.131
    }
    response = requests.post(url, params)
    response.raise_for_status()
    return response.json()


def get_random_comics():
    random_num = random.randrange(2000)
    url = f'https://xkcd.com/{random_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()

    image = response.json()['img']
    filename = response.json()['safe_title']
    alt = response.json()['alt']
    return image, filename, alt


def main():
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    group_id = os.getenv("GROUP_ID")
    vk_access_token = os.getenv("VK_ACCESS_TOKEN")
    os.mkdir("comics")

    comics_image, comics_filename, comics_alt = get_random_comics()
    comics_filepath = f"comics/{comics_filename}.png"

    download_image(comics_image, comics_filepath)
    upload_url = get_upload_url(vk_access_token, group_id)
    
    comics_photo, vk_server, comics_hash = upload_comics(upload_url, comics_filepath)

    media_id, owner_id = upload_comics_on_wall(vk_access_token, group_id, comics_photo, vk_server, comics_hash)

    print(publsih_comics_on_wall(vk_access_token, group_id, client_id, owner_id, comics_alt, media_id))
    os.remove(comics_filepath)
    os.rmdir("comics")
if __name__ == "__main__":
    main()
