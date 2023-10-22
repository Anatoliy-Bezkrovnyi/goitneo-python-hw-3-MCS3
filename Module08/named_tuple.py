import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    list_cats = list()
    if isinstance(cats[0], dict):        
        for dictionary in cats:
            cats_tuple = collections.namedtuple("Cat", dictionary.keys())(*dictionary.values())
            list_cats.append(cats_tuple)
        return list_cats
    if isinstance(cats[0], tuple):
        for item in cats:
            list_cats.append(dict(item._asdict()))
        return list_cats


cats = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
cats1 = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
print(convert_list(cats))