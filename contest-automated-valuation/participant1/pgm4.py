import math
s = raw_input()
pos = [0,0]
s=s.split(',')
i=0
while(i<len(s)):
    movement = s[i].split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
    i+=1

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))
