import json
import pickle


with open('group.json', 'r', encoding='utf-8') as f1:
    json_group = json.load(f1)
    print(json_group)

with open('group.pickle', 'rb') as f2:
    pickle_group = pickle.load(f2)
    print(pickle_group)
