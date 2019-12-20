'''
when defining a function this is the order the parameters

1 - named parameters
2 - *args
3 - named parameters with default values
4 - **kwargs
'''

def parm_order(named_param1, named_parm2, *args, def1='default 1', **kwargs):
    print ([named_param1, named_parm2, args, def1, kwargs])

parm_order('one', 2, 'arg1', 'arg2', 'arg3', def1='default value changed', key1='value1', key2='value2')
