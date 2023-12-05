import requests

from bin.ProjectInfo import PI

def get_upload_server():
    headers = {
        'accept-encoding': '*'
    }
    
    response = requests.post("https://api.vk.com/method/audio.getUploadServer", headers=headers, params={
        "access_token": PI.access_token,
        "v": 5.131
    })

    return response.json()

def upload_audio(url, data):
    file = {
        "file": open(f"{PI.src_dir}\\{data['file_name']}.mp3", "rb")
    }
    
    headers = {
        'accept-encoding': '*'
    }
    
    response = requests.post(url, files=file, headers=headers, params={
        "access_token": PI.access_token,
        "v": 5.131
    })
    
    return response.json()

def save_audio(upload_data):
    response = requests.post("https://api.vk.com/method/audio.save", params={
        "access_token": PI.access_token,
        "server": upload_data["server"],
        "audio": upload_data["audio"],
        "hash": upload_data["hash"],
        "v": 5.131
    })
    
    return response.json()
