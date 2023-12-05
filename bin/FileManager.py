import time
import os

from bin.ProjectInfo import PI

def get_count_similar_files(file_name, dir=PI.src_dir):
    files = os.listdir(dir)
    count = 0
    
    for file in files:
        if file[:len(file_name)] == file_name:
            count += 1
    
    return count

def remove_file(path) -> None:
    for i in range(30):
        try:
            os.remove(path)
            break
        except:
            time.sleep(1.5)
            continue

def get_data_txt(path=f"{PI.current_dir}\\urls.txt") -> dict:
    data_dict = dict()

    with open(path, "r", encoding="UTF-8") as file:
        read_file = file.readlines()

    for num, data in enumerate(read_file):
        data_array = data.split(" ")
        data_dict[num] = dict()
        data_dict[num]["url"] = data_array[0]
        
        for i in data_array[1:]:
            if "=" in i:
                key, value = i.replace("\n", "").split("=")
                data_dict[num][key] = value

    return data_dict
