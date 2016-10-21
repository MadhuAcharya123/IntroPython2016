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

def dict_values(dict):
    all_values = dict.values()
    return all_values

if __name__ == '__main__':
    print("\n") #inserting a newline character for better readability#

    print("The dictionary to start with:")
    display_dict(d)

    print("\n") #inserting a newline character for readability#

    print("The dictionary after deleting the entry for cake:")
    b = delete_dict(d,'cake')
    display_dict(b)

    print("\n") #inserting a newline character for readability#

    print("The dictionary after adding a new fruit called Mango:")
    c = add_dict(b,'fruits','Mango')
    display_dict(c)

    print("\n") #inserting a newline character for readability#

    print("The keys in the dictionary are:")
    dict_key_values(c)

    print("\n") #inserting a newline character for readability#

    print("The values in the dictionary are:")
    d = dict_values(c)
    print(d)

    print("\n") #inserting a newline character for readability#

