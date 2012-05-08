from numpy import *
import pdb
from mathCode import *

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

def stdForm(H):
    print shape(H)
    [n,q]=shape(H)
    #need n*n matrix to be identity

    #make sure that the diagonal has all ones
    for i in range(n):
        if H[i,i]==0:
            for j in range(n):
                if H[j,i]==1:
                    H[i,:]=H[j,:]
    print "No 0's?"
    #print H               

    #make left side all zeros
    for i in range(n):#go through columns
        for j in range(i+1,n):#go through each row in column that is less than the column number
            if H[j,i]==1:
                H[j,:]=binary(H[j,:]+H[i,:])
    #make right side all zeros
    #for i in range(n,0): #go through columns
        #for j in range(n,i-1): #go through each row in column
            #if H[j,i]==1:
                #H[j,:]=H[i,:]   
    return H


H=generate_ldpc(7,14)
H=stdForm(H)
print H
