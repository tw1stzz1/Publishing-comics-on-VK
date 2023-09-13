import requests
import os
import random
from pathlib import Path

from dotenv import load_dotenv


def get_random_comics():
    random_comics = random.randrange(2819)
    url = f'https://xkcd.com/{random_comics}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()

    answer = response.json()
    image = answer['img']
    filename = answer['safe_title']
    alt = answer['alt']
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
    answer = response.json()
    check_response(answer)
    upload_url = answer['response']['upload_url']
    return upload_url


def upload_comics(upload_url, comics_filepath):
    with open(comics_filepath, 'rb') as file:
        url = upload_url
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
    response.raise_for_status() 
    answer = response.json()
    check_response(answer)
    photo = answer['photo']
    server = answer['server']
    comics_hash = answer['hash']
    return photo, server, comics_hash


def upload_comics_on_wall(vk_access_token, group_id, photo, vk_server, comisc_hash):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token" : vk_access_token,
        "group_id" : group_id,
        "photo" : photo,
        "server" : vk_server,
        "hash" : comisc_hash,
        "v" : 5.131
    }
    response = requests.post(url, params)
    response.raise_for_status()
    answer = response.json()
    check_response(answer)
    media_id = answer['response'][0]['id']
    owner_id = answer['response'][0]['owner_id']
    return media_id, owner_id


def publsih_comics_on_wall(vk_access_token, group_id, owner_id, alt, media_id):
    url = "https://api.vk.com/method/wall.post"
    attachments = f"photo{owner_id}_{media_id}" 
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
    answer = response.json()
    check_response(answer)
    return answer


def check_response(response):
    if "error" in response:
        error_code = response["error"]["error_code"]
        error_msg = response["error"]["error_msg"]
        raise requests.HTTPError(error_code, error_msg)


def main():
    load_dotenv()
    group_id = os.getenv("GROUP_ID")
    vk_access_token = os.getenv("VK_ACCESS_TOKEN")
    Path("comics").mkdir(parents=True, exist_ok=True)

    comics_image, comics_filename, comics_alt = get_random_comics()
    comics_filename = f"{comics_filename}.png"
    comics_filepath = os.path.join("comics", comics_filename)
    comics_filepath = comics_filepath.replace("\\", "/")
    try:
        download_image(comics_image, comics_filepath)
        upload_url = get_upload_url(vk_access_token, group_id)
    
        
        comics_photo, vk_server, comics_hash = upload_comics(upload_url, comics_filepath)

        media_id, owner_id = upload_comics_on_wall(vk_access_token, group_id, comics_photo, vk_server, comics_hash)

        publsih_comics_on_wall(vk_access_token, group_id, owner_id, comics_alt, media_id)
    finally:
        os.remove(comics_filepath)

        
if __name__ == "__main__":
    main()
