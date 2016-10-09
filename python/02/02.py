# algo rewrite -Serg
def answer(x,y):
        count = 1
        x_step = 2
        y_step = x

        for x in range(1,x):
                count += x_step
                x_step += 1

        for y in range(1,y):
                count += y_step
                y_step += 1

        #return value
        return count

#initialize prisoners string
prisoners = ""
x = 1
y = 1

#set end condition
fertig = 0
while fertig != 1:

        #reset x = 1, clear line
        x = 1
        prisoner_line = ""

        #do while result < 100000
        while answer(x,y) < 100000:
                prisoner_line =  prisoner_line  +str(answer(x,y))  + ','
                #debug x,y = value
                print(str(x) + ',' + str(y) + ' = ' + str(answer(x,y)))
                x += 1
                
        #next row, check if x = 1 is valid
        y += 1
        if answer(1,y) > 100000:
                fertig = 1

        #append line
        prisoners =  prisoner_line + '\n'  + prisoners
        
#print display
print(prisoners) 

#print to bunny.csv
f1 = open('./bunny.csv', 'w+')
f1.write(prisoners)
f1.close()
