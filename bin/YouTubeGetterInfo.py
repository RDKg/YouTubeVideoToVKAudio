import eyed3
import time
import os
import re
import subprocess
import json

import datetime
import uuid

from bin.ProjectInfo import PI

def get_info_video(url, file_name, title, artist, start, end) -> dict:
    if 'm.youtube.com' in url:
        regex_url = re.findall(r'v=[\^0-9a-z_A-Z-]{1,100}', url)
    elif 'youtu.be' in url:
        regex_url = re.findall(r'be/[\^0-9a-z_A-Z-]{1,100}', url)
    elif 'youtube.com' in url:
        regex_url = re.findall(r'v=[\^0-9a-z_A-Z-]{1,100}', url)
    else: 
        return None

    if len(regex_url) == 0:
        return None
    
    video_id = regex_url[0][2:]

    shell_info = subprocess.Popen(f'"{PI.lib_dir}\\youtube-dl.exe" -s --print-json {url}', cwd=PI.lib_dir, 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    video_info = json.loads(shell_info.communicate()[0].decode('UTF-8'))

    if title == None:
        title = video_info['title']
    if artist == None:
        artist = video_info['channel']
    if file_name == None:
        file_name = video_id
        
    uuid1 = uuid.uuid1()
    file_name = f'{file_name}_{uuid1}'
    
    return {
        'url': f'https://www.youtube.com/watch?v={video_id}',
        'title': title,
        'artist': artist,
        'start': start,
        'end': end,
        'file_name': file_name,
        'video_id': video_id
    }

def get_audio_from_video(data):
    for i in range(10):
        try:
            file_name = data['file_name']
            file_path = f'{PI.src_dir}\\{file_name}.mp3'
            
            if os.path.exists(file_path):
                os.remove(file_path)

            url = data['url']
            start = data['start']
            end = data['end']
            
            yt_cmd = f'"{PI.lib_dir}/youtube-dl.exe" -i -g {url}'
            download_link = subprocess.check_output(yt_cmd, shell=True, timeout=60).decode().split('\n')[1]
            
            ffmpeg_cmd = f'"{PI.lib_dir}/ffmpeg" -i "{download_link}" -ss {start} -to {end} -b:a 384k -vn "{file_path}"'
            subprocess.call(ffmpeg_cmd, shell=True)

            file_tags = eyed3.load(file_path)
            file_tags.tag.artist = data['artist']
            file_tags.tag.title = data['title']
            file_tags.tag.save()
        
            break
        except Exception as exception:
            continue
    else:
        raise Exception()