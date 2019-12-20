def position(pos):
    # print (pos)
    rtn = 'Unknown'
    if pos == 'P':
        rtn = 'Pitcher'
    elif pos == 'C':
        rtn = 'Catcher'
    elif pos in ('1B', 'B1'):
        rtn = '1st Baseman'
    elif pos in ('2B', 'B2'):
        rtn = '2nd Baseman'
    elif pos in ('3B', 'B3'):
        rtn = '3rd Baseman'
    elif pos == 'SS':
        rtn = 'Shortstop'
    elif pos == 'LF':
        rtn = 'Left fielder'
    elif pos == 'CF':
        rtn = 'Center fielder'
    elif pos == 'RF':
        rtn = 'Right fielder'
    return rtn

def lineup(**kwargs):
    print('------')
    print('Lineup')
    print('------')

    for k,v in kwargs.items():
        p = position(k)
        print(f'{v} - {p}')

lineup(LF='Arno', SS='Raul', P='Juan Carlos', CF='Elio', C='Diego', B3='Bill', B1='Carlos', B2='Papo', RF='Christophe')
