def impl(w, y):
    #if w == 1 and y == 0:
        #return 0
    #return 1
    return (not w) or y

def f(x, y, z, w):
    return (not x) and (w == (not z)) and impl(w, y)

for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            for w in range (0, 2):
                value = int(f(x,y,z,w))
                if value == 1:
                    #print(x, y, z, w, value)
                    print(w, y, x, z, value)

#for w in range (0, 2):
#    for y in range (0, 2):
#        for x in range (0, 2):
#            for z in range (0, 2):
#                value = int(f(w,y,x,z))
#                if value == 1:
#                    print(w, y, x, z, value)

