def hplist(iterable, ncols=3, spacing=None, ispacing=1):
    if ispacing is not None:
        spacing = max(len(str(i)) for i in iterable) + ispacing

    for i, item in enumerate(iterable):
        if (i+1)%ncols==0: 
            print(str(item), end='\n')
        else:
            print(str(item).ljust(spacing), end='')

def plist(iterable, ncols=3, spacing=None, ispacing=1):
    list_iterable = list(iterable)
    len_iterable = len(list_iterable)
    
    if spacing is None:
        mxlen = max(len(str(i)) for i in list_iterable)
        spacing = mxlen+ispacing
    
    # items per column
    ipc = len_iterable//ncols + (len_iterable%ncols != 0)
    
    for row in range(ipc):
        items = list_iterable[row::ipc]
        hplist(items, len(items), spacing)