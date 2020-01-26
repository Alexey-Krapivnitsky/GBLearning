import json
import pickle

my_favourite_group = {
    'name': 'Кино',
    'tracks': ['Перемен', 'Последний герой', 'Группа крови'],
    'Albums': [{'name': 'Последний герой', 'year': 1989},
               {'name': 'Группа крови', 'year': 1988}]
}

json_fav_group = json.dumps(my_favourite_group)
pickle_fav_group = pickle.dumps(my_favourite_group)
print(json_fav_group)
print(pickle_fav_group)

with open('group.json', 'w', encoding='utf-8') as f1:
    json.dump(my_favourite_group, f1, ensure_ascii=False)

with open('group.pickle', 'wb') as f2:
    pickle.dump(my_favourite_group, f2)
