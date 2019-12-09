import json

class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email


obj = Person("Abc","abc@gmail.com")
json_object = json.dumps(obj.__dict__)
print(json_object)
dict_obj = json.loads(json_object)
print(dict_obj)



