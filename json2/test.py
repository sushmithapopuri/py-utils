import __init__ as json

b = '''[   
    {"name":"Ram", "email":"ram@gmail.com", "age":23},    
    {"name":"Shyam", "email":"shyam23@gmail.com", "age":28},  
    {"name":"John", "email":"john@gmail.com", "age":33},    
    {"name":"Bob", "email":"bob32@gmail.com", "age":41, "bool_check": true}
]'''

j = {
    "Name1": {
        "NNum": "11",
        "Node1": {
            "SubNodeA": "Thomas",
            "SubNodeB": "27"
        },
        "Node2": {
            "SubNodeA": "ZZZ",
            "SubNodeD": "XXX",
            "SubNodeE": "yy"
        },
        "Node3": {
                "child1": 11,
                "child2": {
                    "grandchild": [{
                        "greatgrandchild1": "Rita",
                        "greatgrandchild2": "US"
                                },
                                {"greatgrandchild1": "Rita",
                        "greatgrandchild2": "US",
                        "greatgrandchild3": "USC",

                        }]
                            }   
                }
            }
}

#print(json.get(j,'Name1.Node3.child2.grandchild.[1].greatgrandchild3'))
# print(json.get_keys(j,5,separator = '|',flatten_list = False))
# print(json.flatten_json(j,5))
# r = json.flatten(j['Name1']['Node3'],5,'|', False)


# #Full Test
# a = json.get_keys(j,5,'|')
# print(a)
# bc= json.get_keys(b,3,'}')
# print(b)
    

# print(json.loads(b))
c = json.flatten(j,depth=30, separator='|')
print('c','\n',c,'\n')
print(json.nest(c,depth = 5,separator='|'))