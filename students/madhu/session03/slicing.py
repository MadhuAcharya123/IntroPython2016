def exchange(str):
    print str[-1] + str[1:len(str)] + str[0]
#this will not work for any sequence just for strings
# asser swap('something') == gomethins'

def item_removed(str):
    print str[0:len(str):2]


def slicing3(str):
    str = str[:-4]
    str = str[4:]
    print str[0:len(str):2]


def slicing4(str):
    print str[::-1]

if __name__ == "__main__":
    exchange('this is the slicing lab')
    item_removed('this is the slicing lab')
    slicing3('this is the slicing lab')
    slicing4('this is the slicing lab')
