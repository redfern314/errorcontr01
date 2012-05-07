from numpy import *
import pdb

def generate_ldpc(rows,columns):
    #create a matrix of all zeros
    zeros_array = zeros((rows,columns))
    ldpc = matrix(zeros_array)

    #place 5 randoms 1s in each column
    for i in range(columns):
        for j in range(5):
            randrow=int(random.random()*rows)
            while ldpc[randrow,i]==1:
                randrow=int(random.random()*rows)
            ldpc[randrow,i]=1

    numones=0.0
    zeros_array = zeros((rows,1))
    rowones = matrix(zeros_array)
    for i in range(rows):
        for j in range(columns):
            if ldpc[i,j]==1:
                numones+=1
                rowones[i,0]+=1

    print ldpc
    print rowones
    avgones=numones/rows
    if not int(avgones)==avgones:
        print 'Avg number of ones: ' + str(avgones)
        print 'This is invalid.'
        pdb.set_trace()
    
    for a in range(10):
        templist=[]
        for i in range(rows):
            if rowones[i,0]>avgones:
                randcol=int(random.random()*columns)
                while ldpc[i,randcol]==0:
                    randcol=int(random.random()*columns)
                for j in range(rows):
                    if rowones[j,0]<avgones and (not ldpc[j,randcol]==1) and (not j==i):
                        templist.append(j)
                if not len(templist)==0:
                    randrow=int(random.random()*len(templist))
                    ldpc[i,randcol]=0
                    rowones[i,0]-=1
                    ldpc[templist[randrow],randcol]=1
                    rowones[templist[randrow],0]+=1
            templist=[]

    #ident=matrix(eye(rows))
    #ldpc=concatenate((ident,ldpc),1)
    savetxt('pmatrix.txt',ldpc)
    print ldpc
    print rowones
    return ldpc

generate_ldpc(25,25)