# YouTubeVideoToVKAudio
Конвертирует YouTube-видео в mp3 файл и загружает в ВК.

# **УСТАНОВКА**

*https://github.com/BtbN/FFmpeg-Builds/releases* - установите отсюда файл *ffmpeg-master-latest-win64-gpl.zip*. 

Перетащите файл *ffmpeg.exe* из *ffmpeg-master-latest-win64-gpl.zip/bin/* в *./lib*

# **НАСТРОЙКА**

В файл *config.txt* надо закинуть ссылку, полученную после авторизации на *https://vkhost.github.io/* с настройками, как на скрине ниже.

![image](https://github.com/RDKg/YouTubeVideoToVKAudio/assets/115119289/a4d8a6da-bddf-476f-b5e8-b5886d691ab2)

# **КАК ПОЛЬЗОВАТЬСЯ?**

В файл *urls.txt* каждая строка должна выглядеть примерно так(можно оставить просто ссылку):

*https://www.youtube.com/watch?v=0B9ZpPOSEVI file_name=None title=None artist=None start=00:00:00 end=00:30:00 delete=False upload=True*

# **ПАРАМЕТРЫ**

*file_name* - Название mp3 файла. По умолчанию генерируется рандомный uuid.

*title* - Название аудиозаписи в ВК. По умолчанию берется с YouTube-видео.

*artist* - Название исполнителя аудиозаписи в ВК. По умолчанию берется с названия канала автора YouTube-видео.

*start* - С какого момента начнется аудиозапись. По умолчанию 00:00:00 (Часы:Минуты:Секунды)

*end* - На каком моменте закончится аудиозапись. По умолчанию 00:30:00 (Часы:Минуты:Секунды)

*delete* - Проверяет удалить ли файл после завершения всех операций. По умолчанию файл не будет удаляться.

*upload* - Проверяет загрузить ли файл в ВК. По умолчанию файл будет загружаться.
