a={'physics':82,'math':65,'history':75}
max=0
min=0
if a['physics']>a['math']:
    if a['physics']>a['history']:
        max=a['physics'].keys()
    else:
        max=a['history'].keys()
else:
    if a['math']>a['history']:
        max=a['math'].keys()
    else:
        max=a['history'].keys()
if a['physics']<a['math']:
    if a['physics']<a['history']:
        min=a['physics'].keys()
    else:
        min=a['history'].keys()
else:
    if a['math']<a['history']:
        min=a['math'].keys()
    else:
        min=a['history'].keys()     
print('Maximum:',max)
print("Minimum:",min)        
        
        