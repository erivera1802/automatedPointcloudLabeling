import os
import pickle

def count_elements_in_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        return len(data)

def total_elements_in_folder(folder_path):
    total_elements = 0
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pkl'):
            file_path = os.path.join(folder_path, file_name)
            current_len = count_elements_in_pickle(file_path)
            total_elements += current_len
            print(f'Total number of current {file_name} : {current_len}')
    
    return total_elements

# Example usage:
folder_path = '/MS3D/tools/cfgs/target_custom/label_generation/round1_automated_pipeline/ps_labels'
total_elements = total_elements_in_folder(folder_path)
print(f'Total number of elements in all .pkl files: {total_elements}')
