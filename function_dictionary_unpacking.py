'''function_dictionary_unpacking.py
this unpacks args and dictionary
'''

def battery(*args):
    def batterymen(pitcher, catcher):
        print(f'The pitcher is {pitcher} and his catcher is {catcher}')

    # dictionaries are looped
    for batteries in args:
        batterymen(**batteries) # each dictionary is unpacked

b = [{'pitcher':'Juan Carlos','catcher':'Victor'}, {'pitcher':'Guillaume','catcher':'Cedric'}]
battery(*b) # unpack a list containing dictionaries

