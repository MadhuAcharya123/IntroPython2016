d = {'name':'Chris','city':'Seattle','cake':'Chocolate'}

def display_dict(dict):
    for k, v in dict.items():
        print("%s: %s" % (k,v))

def delete_dict(dict,key):
    del dict[key]
    return dict

def add_dict(dict,key,value):
    dict[key] = value
    return dict

def dict_key_values(dict):
    all_keys = dict.keys()
    print all_keys

if __name__ == '__main__':
    print("The dictionary to start with:")
    display_dict(d)
    print("The dictionary after deleting the entry for cake:")
    b = delete_dict(d,'cake')
    display_dict(b)
    print("The dictionary after adding a new fruit called Mango:")
    c = add_dict(b,'fruits','Mango')
    display_dict(c)
    print("The key values in a dictionary are:")
    dict_key_values(c)

