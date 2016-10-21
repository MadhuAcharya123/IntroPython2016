#!/usr/bin/env python3

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

def is_key(di,ke):
    """Display whether or not cake is a key in the dictionary."""
    if ke in di.keys():
        return True
    else:
        return False

def is_value(di,val):
    """Display whether or not Mango is a value in the dictionary."""
    if val in di.values():
        return True
    else:
        return False



# Set Datatype Operations #


def create_sets():
    """Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4."
    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(21):
        if i%4 == 0:
            s4.add(i)
        elif i%3 == 0:
            s3.add(i)
        elif i%2 ==0:
            s2.add(i)
    print(s2)
    print(s3)
    print(s4)




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

    print("\n") #inserting a newline character for better readability#

    print('Display whether or not "cake" is a key in the dictionary')
    e = is_key(c,'cake')
    print(e)

    print("\n") #inserting a newline character for better readability#

    print('Display whether or not "Mango" is a value in the dictionary')
    f = is_value(c,'Mango')
    print(f)

    create_sets()

    print("\n") #inserting a newline character for readability#

