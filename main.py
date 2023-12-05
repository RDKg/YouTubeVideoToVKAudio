import concurrent.futures

from bin.__init__ import *
from bin.ProjectInfo import PI

def main(
    url=None, 
    file_name=None, 
    title=None, 
    artist=None, 
    start='00:00:00', 
    end='00:30:00', 
    delete=False, 
    upload=True
):
    data = get_info_video(url, file_name, title, artist, start, end)

    try:
        get_audio_from_video(data)
        print(f'Установлено: {url}')

        if upload:
            upload_server = get_upload_server()
            upload_url = upload_server['response']['upload_url']
            upload_data = upload_audio(upload_url, data)
            saved_audio = save_audio(upload_data)
            log = f'{upload_server, upload_data, saved_audio}'
            
            print(f'Добавлено: {url}')
    except Exception as ex:
        log = ex
        print(f'Произошла ошибка: {url}')
    finally:
        if delete:
            remove_file(f'{PI.current_dir}\\src\\{data["videoID"]}.mp3')
            
    with open('logs.txt', 'a') as file:
        file.writelines(f'url: {url.replace(os.linesep, "")}\Log: {log}\n\n')

if __name__ == '__main__':
    data = get_data_txt()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for key in data:
            file_name = data[key].get('file_name', None)
            url = data[key].get('url', None)
            title = data[key].get('title', None)
            artist = data[key].get('artist', None)
            start = data[key].get('start', '00:00:00')
            end = data[key].get('end', '00:30:00')
            delete = data[key].get('delete', False) == True
            upload = data[key].get('upload', True) == True

            executor.submit(main, url, file_name, title, artist, start, end, delete, upload)