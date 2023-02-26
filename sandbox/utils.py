import json

def load_data_from_json(file_path):
    with open(file_path, 'r') as openfile:
        stories = json.load(openfile)
    return stories