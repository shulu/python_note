# -*- coding: utf-8 -*-

import pickle,json

d =dict(name='bob', age=20, score=88)

print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

print(json.dumps(d))
json_str = '{"name": "bob", "age": 20, "score": 88}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def studen2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

print(json.dumps(s, default=studen2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2student))