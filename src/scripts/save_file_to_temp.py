import os
from src.scripts.create_directory import create_directory_if_not_exits

def save_file_to_temp(file,dir_name) : 
    target_dir = create_directory_if_not_exits(dir_name)
    
    target_path = os.path.join(target_dir,file.filename)
    
    file.save(target_path)
    
    return target_path