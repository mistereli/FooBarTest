def answer(start, length):
    
    #get total num of args
    arg = length
    total_arg = 0
    while arg > 0:
        total_arg += arg
        arg -= 1
    args = range(total_arg)

    #XOR prisoners
    row_pos = 0
    row = 0
    lim = length
    pris = start    
    
    for x in args:
        print('pris = ' + str(pris))
        if x > 0:
            checksum ^= pris
        else:
            checksum = pris
        print('chk = ' + str(checksum))

        #increment row position and check limit
        row_pos += 1
        if row_pos > lim-1:
            row_pos=0
            lim -=1
            row+=1
            pris = start + length*row
        else:
            pris +=1
            
    return checksum

print('final = ' + str(answer(0,3)))
print('-------')
print('final = ' + str(answer(17,4)))
