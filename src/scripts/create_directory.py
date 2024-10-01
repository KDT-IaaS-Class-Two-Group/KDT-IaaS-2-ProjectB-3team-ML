import os

def create_directory_if_not_exits(temp_dir):
    
    current_dir = os.path.dirname(__file__)
    
    target_dir = os.path.join(current_dir, temp_dir)
    
    os.makedirs(target_dir, exist_ok=True)
    
    return target_dir