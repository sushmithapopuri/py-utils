from json import *
import pip

def install_dependencies(package):
    try:
        return __import__(package)
    except ImportError:
        pip.main(['install', package])
    return __import__(package)

a = '''[   
    {"name":"Ram", "email":"ram@gmail.com", "age":23},    
    {"name":"Shyam", "email":"shyam23@gmail.com", "age":28},  
    {"name":"John", "email":"john@gmail.com", "age":33},    
    {"name":"Bob", "email":"bob32@gmail.com", "age":41}   
]'''

b = '''{"a":"2023-08-17,T08:20:28.438Z"}'''

def validate_type(jobject,):
    return type(jobject) in [list,bool,int,None,dict,str]

def validate_json(jobject, schema) -> bool:

    jsonschema = install_dependencies('jsonschema')

    try:
        schema = load(schema)
    except Exception as exception:
        raise Exception('Invalid Schema')
    
    try:
        jsonData = load(jobject)
    except Exception as exception:
        raise Exception('Invalid JSON')
    
    try:
        jsonschema.validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

a = validate_json(open('sample.json','r'),open('sample.schema','r'))

print(a)