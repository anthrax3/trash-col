Program 1
Write a program to find the factorial of two given number
It should be in the given format:
	4 5
	24 120

Solution
num1,num2=map(int,raw_input().split())
fact1=fact2=1
i=1
while i<=num1:
	fact1*=i
	i+=1
i=1
while i<=num2:
	fact2*=i
	i+=1
print fact1,fact2

in.pgm1.txt
	4 5
out_cor.pgm1.txt
	24 120

Checking:
from subprocess import Popen, PIPE, STDOUT
f = open('in.pgm1.txt','r')
corr = open('out_cor.pgm1.txt', 'r')
oppp = []
corr= corr.read().split()
p = Popen(["python","pgm.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate(input=f.read())[0]
oppp.append(out.split()[0])
oppp.append(out.split()[1])

i=0
correct=1
for i in range (0,len(corr)):
	if(corr[i]!=oppp[i]):
		correct=0
if correct==1:
	print "You are done"
else:
	print "failed"

Problem 2
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
	1. At least 1 letter between [a-z]
	2. At least 1 number between [0-9]
	1. At least 1 letter between [A-Z]
	3. At least 1 character from [$#@]
	4. Minimum length of transaction password: 6
	5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
	If the following passwords are given as input to the program:
	ABd1234@1,a F1#,2w3E*,2We3345
	Then, the output of the program should be:
	ABd1234@1

Solution:pgm2.py
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)

in.pgm2.txt
	ABd1234@1,a F1#,2w3E*,2We3345
out_cor.pgm2.txt
	ABd1234@1

Checking:
from subprocess import Popen, PIPE, STDOUT
f = open('in.pgm2.txt','r')
corr = open('out_cor.pgm2.txt', 'r')
oppp = []
corr= corr.read().split()
p = Popen(["python","pgm2.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate(input=f.read())[0]
oppp.append(out.split()[0])

i=0
correct=1
for i in range (0,len(corr)):
	if(corr[i]!=oppp[i]):
		correct=0
if correct==1:
	print "You are done"
else:
	print "failed"

Problem 3:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
	1: Sort based on name;
	2: Then sort based on age;
	3: Then sort by score.
	The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Note: the inputs are to be given using a file(store the inputs to a file named in.pgm3.txt and get the values from it)
Then, the output of the program should be:
[('John', '20', '90\n'), ('Jony', '17', '91\n'), ('Jony', '17', '93\n'), ('Json', '21', '85\n'), ('Tom', '19', '80\n')]

Solution:
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

in.pgm3.txt
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

out_cor.pgm3.txt
[('John', '20', '90\n'), ('Jony', '17', '91\n'), ('Jony', '17', '93\n'), ('Json', '21', '85\n'), ('Tom', '19', '80\n')]

Checking:
from subprocess import Popen, PIPE, STDOUT
corr = open('out_cor.pgm3.txt', 'r')
oppp = []
p = Popen(["python","pgm3.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate()[0]
if out==corr.read():
	print "You are done"
else:
	"Failed"

Problem 4:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
	UP 5
	DOWN 3
	LEFT 3
	RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
	UP 5,DOWN 3,LEFT 3,RIGHT 2
Then, the output of the program should be:
	2

Solution:pgm4.py

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

out_cor.pgm4.txt
	2

Checking:
from subprocess import Popen, PIPE, STDOUT
corr = open('out_cor.pgm4.txt', 'r')
p = Popen(["python","pgm4.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate("UP 5,DOWN 3,LEFT 3,RIGHT 2")[0]
if out==corr.read():
	print "You are done"
else:
	print "failed"

Problem 5:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
	New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
	2:2
	3.:1
	3?:1
	New:1
	Python:5
	Read:1
	and:1
	between:1
	choosing:1
	or:2
	to:1

Solution:pgm5.py
freq = {}
line = raw_input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
	print "%s:%d" % (w,freq[w])

out_cor.pgm5.property
	2:2
	3.:1
	3?:1
	New:1
	Python:5
	Read:1
	and:1
	between:1
	choosing:1
	or:2
	to:1

Checking:
from subprocess import Popen, PIPE, STDOUT
corr = open('out_cor.pgm5.txt', 'r')
p = Popen(["python","pgm5.py"], stdin=PIPE, stdout=PIPE)
out = p.communicate("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")[0]
if out==corr.read():
	print "You are done"
else:
	print "failed"
