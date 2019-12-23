'''
Error handling in Python
'''

def get(dictionary, key):
    '''
    get
    description:
        get the key from a dictionary
    parms:
        dictionary: a dictionary structure
        key: a key in the dictionary
    return:
        the value of the passed dictionary key
    exceptions:
        None: when it's not a valid key
        Invalid arguments: when the arguments are not a dictionary and a string

    '''
    rtn = ''  
    try:
        key_integer = int(key)
        rtn = dictionary[key]
    except KeyError:
        rtn = None
    except TypeError as err:
        rtn = 'Invalid arguments'
        print(err)
    except:
        rtn = 'unknown error'
    else:
        print('*** success')
    finally:
        return rtn

player = {'1': 'Tony', '2':'pitcher'}
player2 = {}
print(get(player, '1'))
print(get(player, '2'))
print(get(player, '3'))
print(get('tony', '1'))
print(get(player, 'not a number'))

