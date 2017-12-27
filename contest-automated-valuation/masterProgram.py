#masterProgram.py
'''
1. For program 3(a program which works using a file, the file location should be in the location where the masterProgram.py lies). So, the input test value should be placed where masterProgram.py is located.
2. So, as the first step, the test sample for this program is to be made available at ..
3. If all the problems are not solved, the result of the respective will be considered as 'incomplete'
'''
'''
variables
    i -- participant number
    k -- for checking correctness for subprograms
    corr -- holds the correct answers -- both file reference and list
    f -- holds input samples
    oppp -- holds return values(outputs)
'''
from subprocess import Popen, PIPE, STDOUT
import os
#store the success list to a file named successList.txt
os.system("cp -f in/in.pgm3.txt .")
successList=open('successList.txt','w')
for i in range(1,4):
    totalCorr=0
    if(len([name for name in os.listdir('participant'+str(i)+'/')]) == 6 ):#(5+1) because the third program requires a file named in.pgm3.txt

        #validating program 1
        programURL="participant"+str(i)+"/pgm1.py"
        #check program 1
        f = open('in/in.pgm1.txt','r')
        corr = open('out_cor/out_cor.pgm1.txt', 'r')
        oppp = []
        corr= corr.read().split()
        p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
        out = p.communicate(input=f.read())[0]
        oppp.append(out.split()[0])
        oppp.append(out.split()[1])

        k=0
        correct=1
        for k in range (0,len(corr)):
        	if(corr[k]!=oppp[k]):
        		correct=0
        if correct==1:
        	totalCorr+=1
        else:
        	totalCorr=totalCorr
        f.close()

        #validating program 2
        programURL="participant"+str(i)+"/pgm2.py"
        f = open('in/in.pgm2.txt','r')
        corr = open('out_cor/out_cor.pgm2.txt', 'r')
        oppp = []
        corr= corr.read().split()
        p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
        out = p.communicate(input=f.read())[0]
        oppp.append(out.split()[0])

        if corr[0]==oppp[0]:
        	totalCorr+=1
        else:
        	totalCorr=totalCorr
        f.close()

        #validating program 3
        programURL="participant"+str(i)+"/pgm3.py"
        corr = open('out_cor/out_cor.pgm3.txt', 'r')
        oppp = []
        p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
        out = p.communicate()[0]
        if out==corr.read():
        	totalCorr+=1
        else:
        	totalCorr=totalCorr
        f.close()

        #validating program 4
        programURL="participant"+str(i)+"/pgm4.py"
        f = open('in/in.pgm4.txt','r')
        corr = open('out_cor/out_cor.pgm4.txt', 'r')
        p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
        out = p.communicate(f.read())[0]
        cor=corr.read()
        if out==cor:
        	totalCorr+=1
        else:
        	totalCorr=totalCorr
        f.close()


        #validating program 5
        programURL="participant"+str(i)+"/pgm5.py"
        f = open('in/in.pgm5.txt','r')
        corr = open('out_cor/out_cor.pgm5.txt', 'r')
        p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
        out = p.communicate(f.read())[0]
        if out==corr.read():
        	totalCorr+=1
        else:
        	totalCorr=totalCorr
        f.close()
    else:
        totalCorr=-1
    if totalCorr==-1:
        successList.write("Participant"+str(i)+"\tCorrect : Incomplete\n")
    else:
        successList.write("Participant"+str(i)+"\tCorrect : "+str(totalCorr)+"\n")
successList.close()
os.system("cat successList.txt")
os.system("rm -f in.pgm3.txt")

'''
different test samples can be used or multiple tests can be made by multiple use of the statements and corrsponding validations..
p = Popen(["python",programURL], stdin=PIPE, stdout=PIPE)
out = p.communicate(f.read())[0]
'''
