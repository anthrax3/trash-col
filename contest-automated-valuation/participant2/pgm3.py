from operator import itemgetter
l = []
f=open('in.pgm3.txt','r')
while True:
    s = f.readline()
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,1,2))
f.close()
