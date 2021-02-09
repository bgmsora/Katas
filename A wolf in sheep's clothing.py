def warn_the_sheep(queue):
    band=0
    z=0
    for x in queue:
        if band==1:
            z+=1
        if x=='wolf':
            band=1
            
    if z!=0:
        return 'Oi! Sheep number '+str(z)+'! You are about to be eaten by a wolf!'
    else:
        return 'Pls go away and stop eating my sheep'